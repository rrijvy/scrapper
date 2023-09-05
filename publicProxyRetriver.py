import requests
import json

sources = list(
    map(
        lambda x: x.replace("\n", ""),
        open("sources.txt", "r", encoding="UTF-8").readlines(),
    )
)

session = requests.Session()
session.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
)

proxies: list[str] = []

for source in sources:
    response = session.get(source).text.splitlines()
    proxies.extend(response)

validProxies: list[str] = []

for proxy in proxies:
    response = session.get("http://httpbin.org/ip")
    if response.status_code == 200:
        print(proxy)
        validProxies.append(proxy)

with open("proxies.json", "w") as json_file:
    json.dump(proxies, json_file, indent=4)

with open("proxies.json", "r") as json_file:
    proxyList = json.load(json_file)
