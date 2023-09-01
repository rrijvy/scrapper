import json
from amazonCrawler import AmazonCrawler
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

url = "https://www.amazon.com/Razer-Kraken-Ultralight-Gaming-Headset/dp/B09SJWCKL4/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&keywords=gaming+headsets&pd_rd_r=a4b00db6-1e8f-4852-9d78-89e4816b0add&pd_rd_w=BVDk0&pd_rd_wg=3EH2S&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=K9RNEBAGYNSS8XNKWC1Z&qid=1693602635&sr=8-1"

crawler = Crawler()
crawler.initRequest(url, userAgents, proxies, AmazonCrawler())
