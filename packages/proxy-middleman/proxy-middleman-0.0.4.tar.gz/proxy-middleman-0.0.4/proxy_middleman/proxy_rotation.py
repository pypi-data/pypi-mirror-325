import asyncio
import random
import time
import apprise
from curl_cffi import requests



class ProxyMiddleman:
    def __init__(self, connectors_ids: list[str], number_of_retries=3, backoff_time=10, exponential_backoff=True, slack_webhook_url=None):
        """
        Initializes the ProxyMiddleman instance with configuration parameters.

        :param connectors_ids: The IDs of the connectors to use.
        :param number_of_retries: Number of retries for proxy requests.
        :param backoff_time: Base time for backoff in seconds.
        :param exponential_backoff: Boolean indicating if exponential backoff should be used.
        :param slack_webhook_url: The URL of the Slack webhook to use for notifications.
        """
        self.connectors = {}  # Save connectors as {connector_id: proxies}
        self.number_of_retries = number_of_retries
        self.backoff_time = backoff_time
        self.exponential_backoff = exponential_backoff
        self.lock = asyncio.Lock()
        
        for connector_id in connectors_ids:
            self.connectors[connector_id] = self.initialize_proxies(connector_id)

        self.apprise_obj = None

        if slack_webhook_url:
            self.apprise_obj = apprise.Apprise()
            self.apprise_obj.add(slack_webhook_url)

    def initialize_proxies(self, connector_id):
        """
        Requests and initializes a list of proxies for a specific connector_id.

        :param connector_id: The ID of the connector for which to initialize proxies.
        :return: A dictionary of proxies with their metadata, filtered by those with status "STARTED".
        :raises Exception: If no proxies are found for the given connector_id.
        """
        response = requests.request(method="GET", url="http://185.253.7.140:8080/proxies", params={"connector_id": connector_id})
        for data in response.json():
            if data["connector"]["id"] == connector_id:
                proxies = data["proxies"]
                break
        else:
            raise Exception(f"No proxies found for connector_id {connector_id}")

        return {
            proxy["name"]: {
                "fails": 0,
                "disabled_until": None,
                "added_at": time.time(),
                "request_count": 0,
                "traffic": 0  # In bytes
            }
            for proxy in proxies
            if proxy["status"] == "STARTED"
        }

    async def get_proxy(self):
        """
        Chooses a random available proxy from first available connector.

        :return: A tuple containing the connector_id and proxy name.
        :raises Exception: If no available proxies or connectors are found after retries.
        """
        while True:
            async with self.lock:
                current_time = time.time()

                for connector_id, proxies in self.connectors.items():
                    available_proxies = [
                        p for p, meta in proxies.items()
                        if meta["disabled_until"] is None or meta["disabled_until"] < current_time
                    ]

                    if available_proxies:
                        return connector_id, random.choice(available_proxies)  # Take random proxy from first available connector

                self.notify("No available proxies! Sleeping for 5 minutes...", notify_type=apprise.NotifyType.WARNING)
                await asyncio.sleep(300)  # Wait 5 minutes before trying again

    async def disable_proxy(self, connector_id, proxy):
        """
        Turns off the proxy for a given connector_id and proxy.

        :param connector_id: The ID of the connector containing the proxy.
        :param proxy: The name of the proxy to disable.
        """
        async with self.lock:
            if connector_id in self.connectors and proxy in self.connectors[connector_id]:
                fails = self.connectors[connector_id][proxy]["fails"]
                backoff = self.backoff_time * (2 ** fails) if self.exponential_backoff else self.backoff_time
                self.connectors[connector_id][proxy]["disabled_until"] = time.time() + backoff
                self.connectors[connector_id][proxy]["fails"] += 1
    
    async def request(self, url, method="GET", **kwargs):
        """
        Sends an HTTP request using a proxy, with retries on failure.

        :param url: The URL to send the request to.
        :param method: The HTTP method to use (default is "GET").
        :param kwargs: Additional arguments to pass to the request.
        :return: The HTTP response object.
        :raises Exception: If all proxies fail after the specified number of retries.
        """
        for _ in range(self.number_of_retries):
            connector_id, proxy = await self.get_proxy()
            try:
                response = requests.request(method, url, proxy=proxy, **kwargs)
                response_size = len(response.content)
                
                async with self.lock:
                    self.connectors[connector_id][proxy]["request_count"] += 1
                    self.connectors[connector_id][proxy]["traffic"] += response_size
                
                if response.status_code in [401, 403, 451, 503]:
                    self.notify(f"Proxy '{proxy}' is disabled due to status code {response.status_code}. Response text: {response.text}", notify_type=apprise.NotifyType.WARNING)
                    await self.disable_proxy(connector_id, proxy)
                    continue
                return response
            except Exception as e:
                self.notify(f"Proxy '{proxy}' is disabled due to unexpected error: {e}", notify_type=apprise.NotifyType.WARNING)
                await self.disable_proxy(connector_id, proxy)
        
        self.notify(f"{self.number_of_retries} attempts were made to send a request using a proxy and none of them passed. Raising an exception on the backend", notify_type=apprise.NotifyType.ERROR)
        raise Exception(f"{self.number_of_retries} attempts were made to send a request using a proxy and none of them passed. Raising an exception on the backend")
        
    def notify(self, message, notify_type=apprise.NotifyType.INFO):
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

        :return: A dictionary containing statistics for each proxy, including request count, traffic, lifetime, and fails.
        """
        return {
            connector_id: {
                proxy: {
                        "request_count": meta["request_count"],
                        "traffic_kb": round(meta["traffic"] / 1024, 2),
                        "lifetime_minutes": round((time.time() - meta["added_at"]) / 60, 2),
                        "fails": meta["fails"],
                        "disabled_until": meta["disabled_until"]
                    }
                    for proxy, meta in proxies.items()
                }
                for connector_id, proxies in self.connectors.items()
            }
