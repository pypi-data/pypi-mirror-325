import asyncio
import random
import time
import apprise
from curl_cffi import requests


apprise_obj = apprise.Apprise()
apprise_obj.add('https://hooks.slack.com/services/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')


class ProxyMiddleman:
    def __init__(self, connector_id=None, number_of_retries=3, backoff_time=10, exponential_backoff=True, proxy_lifetime=10):
        self.connectors = {}  # Save connectors as {connector_id: proxies}
        self.number_of_retries = number_of_retries
        self.backoff_time = backoff_time
        self.exponential_backoff = exponential_backoff
        self.proxy_lifetime = proxy_lifetime * 60  # Convert to seconds
        self.lock = asyncio.Lock()

        if connector_id is None:
            connector_id = self.find_available_connector()
        
        self.connectors[connector_id] = self.initialize_proxies(connector_id)

    def find_available_connector(self):
        """Selects the first available connector_id that is not in self.connectors.keys()."""
        response = requests.request(method="GET", url="http://185.253.7.140:8080/proxies")
        available_connectors = {c["connector"]["id"] for c in response.json()}
        print("available_connectors =", available_connectors)
        used_connectors = set(self.connectors.keys())
        
        unused_connectors = available_connectors - used_connectors
        if not unused_connectors:
            raise Exception("No available connectors to use!")

        return unused_connectors.pop()

    def initialize_proxies(self, connector_id):
        """Requests and initializes a list of proxies for a specific connector_id."""
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
        Chooses a random available proxy from all connectors.
        If no proxies are available, it searches for a new connector.
        """
        while True:
            async with self.lock:
                current_time = time.time()
                available_proxies = [
                    (connector_id, p)
                    for connector_id, proxies in self.connectors.items()
                    for p, meta in proxies.items()
                    if (meta["disabled_until"] is None or meta["disabled_until"] < current_time)
                    and (current_time - meta["added_at"] < self.proxy_lifetime)
                ]

                if available_proxies:
                    return random.choice(available_proxies)  # Returns (connector_id, proxy)

                try:
                    new_connector_id = self.find_available_connector()
                    self.connectors[new_connector_id] = self.initialize_proxies(new_connector_id)
                    self.notify(f"Added new connector {new_connector_id} with proxies.")
                    continue  # After adding a new connector, check again immediately
                except Exception:
                    self.notify("No available proxies and no new connectors! Sleeping for 5 minutes...")
                    await asyncio.sleep(300)  # Wait 5 minutes before trying again

    async def disable_proxy(self, connector_id, proxy):
        """Turns off the proxy for a given connector_id and proxy."""
        async with self.lock:
            if connector_id in self.connectors and proxy in self.connectors[connector_id]:
                fails = self.connectors[connector_id][proxy]["fails"]
                backoff = self.backoff_time * (2 ** fails) if self.exponential_backoff else self.backoff_time
                self.connectors[connector_id][proxy]["disabled_until"] = time.time() + backoff
                self.connectors[connector_id][proxy]["fails"] += 1
    
    async def request(self, url, method="GET", **kwargs):
        for _ in range(self.number_of_retries):
            connector_id, proxy = await self.get_proxy()
            try:
                response = requests.request(method, url, proxy=proxy, **kwargs)
                response_size = len(response.content)
                
                async with self.lock:
                    self.connectors[connector_id][proxy]["request_count"] += 1
                    self.connectors[connector_id][proxy]["traffic"] += response_size
                
                if response.status_code in [401, 403, 451, 503]:
                    await self.disable_proxy(connector_id, proxy)
                    continue
                return response
            except Exception:
                await self.disable_proxy(connector_id, proxy)
        
        self.notify("All proxies failed")
        raise Exception("All proxies failed")
        
    def notify(self, message):
        try:
            apprise_obj.notify(
                body=message,
                title=f"Middleman Proxy Info",
                notify_type=apprise.NotifyType.INFO
            )
        except Exception as e:
            print(f"Error sending notification: {e}")

    def get_proxy_stats(self):
        """Returns statistics for all proxies in all connectors."""
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


# Test cases

async def disable_all_proxies(proxy_manager):
    """Отключает все прокси в текущем коннекторе, чтобы принудительно запустить find_available_connector."""
    async with proxy_manager.lock:
        current_time = time.time()
        for connector_id, proxies in proxy_manager.connectors.items():
            for proxy in proxies:
                proxies[proxy]["disabled_until"] = current_time + 999999  # Отключаем на долгое время
        print(f"All proxies in connector {connector_id} disabled.")

async def test_find_new_connector():
    proxy_manager = ProxyMiddleman(connector_id="98ed4dae-d05d-4b74-984d-03db14c77666", proxy_lifetime=5)
    
    await disable_all_proxies(proxy_manager)  # Отключаем все прокси
    
    connector_before = list(proxy_manager.connectors.keys())  # Запоминаем текущий коннектор
    print(f"Before: {connector_before}")

    try:
        connector_id, proxy = await proxy_manager.get_proxy()  # Должен найти новый коннектор
        print(f"New connector found: {connector_id}, proxy: {proxy}")
    except Exception as e:
        print(f"Error: {e}")

    connector_after = list(proxy_manager.connectors.keys())  # Проверяем, появился ли новый
    print(f"After: {connector_after}")

# Running tests
async def main():
    # Test proxy request and connector switching
    # await test_find_new_connector()

    # Check the proxy stats
    proxy_manager = ProxyMiddleman(connector_id="98ed4dae-d05d-4b74-984d-03db14c77666", proxy_lifetime=5)

    try:
        response = await proxy_manager.request("http://185.253.7.140:8080/proxies")
        print(response.text)
    except Exception as e:
        print(e)
    
    # Output statistics
    print("Proxy stats:", proxy_manager.get_proxy_stats())

asyncio.run(main())
