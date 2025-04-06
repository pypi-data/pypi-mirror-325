import asyncio
import random
import time
import apprise
from curl_cffi import requests
from curl_cffi.requests.exceptions import ProxyError, ConnectTimeout

from proxy_middleman.custom_exceptions import NoProxiesAvailable, ProxyRetriesExceeded


class ProxyMiddleman:
    def __init__(
            self, 
            connectors_ids: list[str], 
            slack_webhook_url: str, 
            number_of_retries: int = 5, 
            backoff_time: int = 10, 
            exponential_backoff: bool = True,
            use_semaphore: bool = False,
            request_per_proxy: int = 1,
            send_alert_after_unexpected_errors: int = 5
        ):
        """
        Initializes the ProxyMiddleman instance with configuration parameters.

        :param connectors_ids: The IDs of the connectors to use.
        :param number_of_retries: Number of retries for proxy requests.
        :param backoff_time: Base time for backoff in seconds.
        :param exponential_backoff: Boolean indicating if exponential backoff should be used.
        :param slack_webhook_url: The URL of the Slack webhook to use for notifications.
        :param use_semaphore: Boolean indicating if semaphore should be used.
        :param request_per_proxy: Number of requests per proxy.
        :param send_alert_after_unexpected_errors: Number of unexpected errors after which an alert should be sent.
        """
        self.connectors = {}  # Save connectors as {connector_id: proxies}
        self.number_of_retries = number_of_retries
        self.backoff_time = backoff_time
        self.exponential_backoff = exponential_backoff
        self.lock = asyncio.Lock()

        self.use_semaphore = use_semaphore
        self.request_per_proxy = request_per_proxy
        
        self.send_alert_after_unexpected_errors = send_alert_after_unexpected_errors

        for connector_id in connectors_ids:
            self.connectors[connector_id] = self._initialize_proxies(connector_id)
        
        self.apprise_obj = apprise.Apprise()
        self.apprise_obj.add(slack_webhook_url)

    def _initialize_proxies(self, connector_id):
        """
        Requests and initializes a list of proxies for a specific connector_id.

        :param connector_id: The ID of the connector for which to initialize proxies.
        :return: A dictionary of proxies with their metadata, filtered by those with status "STARTED".
        :raises Exception: If no proxies are found for the given connector_id.
        """
        response = requests.request(method="GET", url="http://185.253.7.140:8080/proxies")
        for data in response.json():
            if data["connector_id"] == connector_id:
                proxies = data["proxies"]
                break
        else:
            raise NoProxiesAvailable(connector_id)

        return {
            proxy: {
                "unexpected_fails": 0,
                "proxy_not_working_fails": 0,
                "disabled_until": None,
                "added_at": time.time(),
                "request_count": 0,
            }
            for proxy in proxies
        }

    async def _get_proxy(self):
        """
        Chooses a random available proxy from first available connector.

        :return: A tuple containing the connector_id and proxy name.
        :raises Exception: If no available proxies or connectors are found after retries.
        """
        last_notification_time = 0

        while True:
            async with self.lock:
                current_time = time.time()
                found_proxy = False

                for connector_id, proxies in self.connectors.items():
                    available_proxies = [
                        p for p, meta in proxies.items()
                        if meta["disabled_until"] is None or meta["disabled_until"] < current_time
                    ]

                    if available_proxies:
                        found_proxy = True
                        return connector_id, random.choice(available_proxies), len(available_proxies) * self.request_per_proxy if self.use_semaphore else None

                if not found_proxy:
                    if current_time - last_notification_time >= 300:  # 5 minutes
                        self._notify("No available proxies! Sleeping for 5 minutes...", notify_type=apprise.NotifyType.WARNING)
                        last_notification_time = current_time

                await asyncio.sleep(30)

    async def _disable_proxy(self, connector_id, proxy, unexpected_error=False, proxy_not_working=False, response_text=None):
        """
        Disables a proxy for a given connector_id. If a proxy fails 3 times in a row, it gets removed.

        :param connector_id: The ID of the connector containing the proxy.
        :param proxy: The name of the proxy to disable.
        """
        async with self.lock:
            if connector_id in self.connectors and proxy in self.connectors[connector_id]:
                if unexpected_error:
                    self.connectors[connector_id][proxy]["unexpected_fails"] += 1
                elif proxy_not_working:
                    self.connectors[connector_id][proxy]["proxy_not_working_fails"] += 1
                else:
                    raise ValueError("unexpected_error or proxy_not_working must be True")

                # If the proxy breaks 3 times in a row, delete it
                if self.connectors[connector_id][proxy]["proxy_not_working_fails"] >= 3:
                    self._notify(f"Proxy '{proxy}' removed after 3 consecutive failures. Response text: {response_text}", notify_type=apprise.NotifyType.WARNING)
                    del self.connectors[connector_id][proxy]
                else:
                    # Normal shutdown with backoff
                    max_fails = max(self.connectors[connector_id][proxy]["unexpected_fails"], self.connectors[connector_id][proxy]["proxy_not_working_fails"])
                    backoff = self.backoff_time * (2 ** max_fails) if self.exponential_backoff else self.backoff_time
                    self.connectors[connector_id][proxy]["disabled_until"] = time.time() + backoff

                total_unexpected_fails = sum(proxy_data["unexpected_fails"] for proxy_data in self.connectors[connector_id].values())

                if total_unexpected_fails % self.send_alert_after_unexpected_errors == 0:
                    self._notify(f"There have been {self.send_alert_after_unexpected_errors} unexpected errors. Response text: {response_text}", notify_type=apprise.NotifyType.WARNING)
                
    async def _get_semaphore(self):
        """
        :return: A semaphore for the availble_proxies_count * request_per_proxy.
        """
        _, _, semaphore = await self._get_proxy()
        return asyncio.Semaphore(semaphore)
    
    async def _request(self, url, method="GET", **kwargs):
        """
        Sends an HTTP request using a proxy, with retries on failure.

        :param url: The URL to send the request to.
        :param method: The HTTP method to use (default is "GET").
        :param kwargs: Additional arguments to pass to the request.
        :return: The HTTP response object.
        :raises Exception: If all proxies fail after the specified number of retries.
        """
        for _ in range(self.number_of_retries):
            connector_id, proxy, _ = await self._get_proxy()
            try:
                response = requests.request(method, url, proxy=proxy, **kwargs)
                
                async with self.lock:
                    self.connectors[connector_id][proxy]["request_count"] += 1
                
                if response.status_code in [401, 403, 451, 503, 429]:
                    await self._disable_proxy(connector_id, proxy, unexpected_error=True, response_text=response.text)
                    continue
                return response
            except ConnectTimeout:
                pass
            except ProxyError:
                await self._disable_proxy(connector_id, proxy, proxy_not_working=True, response_text=response.text)
            except Exception:
                await self._disable_proxy(connector_id, proxy, unexpected_error=True, response_text=response.text)
        
        self._notify(f"{self.number_of_retries} attempts were made to send a request using a proxy and none of them passed. Raising an exception on the backend", notify_type=apprise.NotifyType.FAILURE)
        raise ProxyRetriesExceeded(self.number_of_retries) 

    async def request(self, url, method="GET", **kwargs):
        """
        Sends an HTTP request using a proxy, with retries on failure.

        :param url: The URL to send the request to.
        :param method: The HTTP method to use (default is "GET").
        :param kwargs: Additional arguments to pass to the request.
        :return: The HTTP response object.
        :raises Exception: If all proxies fail after the specified number of retries.
        """

        if self.use_semaphore:
            semaphore = await self._get_semaphore()
            async with semaphore:
                return await self._request(url, method, **kwargs)
        else:
            return await self._request(url, method, **kwargs)

    def _notify(self, message, notify_type=apprise.NotifyType.INFO):
        """
        Sends a notification with the given message.

        :param message: The message to include in the notification.
        :param notify_type: The type of the notification.
        """
        try:
            if self.apprise_obj:
                self.apprise_obj.notify(
                    body=message,
                    title="Middleman Proxy Info",
                    notify_type=notify_type
                )
            else:
                print("No apprise object found. Skipping notification")
        except Exception as e:
            print(f"Error sending notification: {e}")

    def get_proxy_stats(self):
        """
        Returns statistics for all proxies in all connectors.

        :return: A dictionary containing statistics for each proxy, including request count, lifetime, and fails.
        """
        return {
            connector_id: {
                proxy: {
                        "request_count": meta["request_count"],
                        "lifetime_minutes": round((time.time() - meta["added_at"]) / 60, 2),
                        "unexpected_fails": meta["unexpected_fails"],
                        "proxy_not_working_fails": meta["proxy_not_working_fails"],
                        "disabled_until": meta["disabled_until"]
                    }
                    for proxy, meta in proxies.items()
                }
                for connector_id, proxies in self.connectors.items()
            }
