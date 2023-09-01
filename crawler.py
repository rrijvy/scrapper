from requests import Session
from abstractCrawler import AbstractCrawler
from proxy import Proxy
from userAgent import UserAgent


class Crawler:
    def initRequest(
        self,
        url: str,
        userAgents: list[UserAgent],
        proxies: list[Proxy],
        crawler: AbstractCrawler,
    ):
        userAgent: UserAgent
        proxy: Proxy

        for agent in userAgents:
            if agent.isActive == False:
                userAgent = agent
                agent.isActive = True
                break

        for proxyItem in proxies:
            if proxyItem.isActive == False:
                proxy = proxyItem
                proxyItem.isActive = True
                break

        requestHeaders = {"User-Agent": userAgent.ua}

        proxyUrls = {
            "http": f"http://{proxy.ip}:{proxy.port}",
            "https": f"https://{proxy.ip}:{proxy.port}",
        }

        requestSession = Session()

        requestSession.headers.update(requestHeaders)

        # requestSession.proxies.update(proxyUrls)

        response = requestSession.get(url)

        isCrawlingSucceeded = crawler.startCrawl(response)

        if isCrawlingSucceeded:
            userAgent.isActive = False
            proxy.isActive = False

        print(isCrawlingSucceeded)
