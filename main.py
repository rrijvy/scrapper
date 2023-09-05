import json
from amazonCrawler import AmazonCrawler
from amazonSearchCrawler import AmazonSearchCrawler
from crawler import Crawler
from proxy import Proxy
from userAgent import UserAgent

with open("user-agents.json", "r") as file:
    jsonAgentData = json.load(file)

with open("proxies.json", "r") as file:
    jsonProxyData = json.load(file)

userAgents: list[UserAgent] = [
    UserAgent(data["ua"], data["pct"]) for data in jsonAgentData
]
proxies: list[Proxy] = [Proxy(data) for data in jsonProxyData]


url = "https://www.amazon.com/s?k=nike+shoe"


crawler = Crawler(url, userAgents, proxies)
crawler.initRequest(AmazonSearchCrawler())

# crawler2 = Crawler(url, userAgents, proxies)
# crawler2.initRequest(AmazonSearchCrawler())
# crawler3 = Crawler(url, userAgents, proxies)
# crawler3.initRequest(AmazonSearchCrawler())
# crawler4 = Crawler(url, userAgents, proxies)
# crawler4.initRequest(AmazonSearchCrawler())
