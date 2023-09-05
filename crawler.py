from requests import Session
from abstractCrawler import AbstractCrawler
from proxy import Proxy
from userAgent import UserAgent


class Crawler:
    userAgents: UserAgent
    proxy: Proxy

    def __init__(
        self,
        url: str,
        userAgents: list[UserAgent],
        proxies: list[Proxy],
    ) -> None:
        self.url: str = url
        self.userAgents: list[UserAgent] = userAgents
        self.proxies: list[Proxy] = proxies
        self.requestSession: Session = Session()
        self.updateRequestHeader()

    def getUserAgent(self) -> UserAgent:
        for agent in self.userAgents:
            if agent.isActive == False:
                agent.isActive = True
                return agent

    def getProxy(self) -> Proxy:
        for proxyItem in self.proxies:
            if proxyItem.isActive == False:
                proxyItem.isActive = True
                return proxyItem

    def updateRequestHeader(self) -> None:
        self.userAgent: UserAgent = self.getUserAgent()
        self.proxy: Proxy = self.getProxy()
        requestHeaders = {"User-Agent": self.userAgent.ua}
        proxyUrls = {"http": f"https://{self.proxy.ip}:{self.proxy.port}"}
        self.requestSession.headers.update(requestHeaders)
        self.requestSession.proxies.update(proxyUrls)

    def retry(self, crawler: AbstractCrawler):
        self.updateRequestHeader()
        response = self.requestSession.get(self.url)
        if response.status_code == 200:
            isCrawlingSucceeded = crawler.startCrawl(response)
        else:
            self.retry(crawler)
        pass

    def initRequest(self, crawler: AbstractCrawler):
        response = self.requestSession.get(self.url)
        if response.status_code == 200:
            isCrawlingSucceeded = crawler.startCrawl(response)
            # self.userAgent.isActive = False
            # self.proxy.isActive = False
        else:
            # self.userAgent.isActive = False
            # self.proxy.isActive = False
            self.retry(crawler)

        print(isCrawlingSucceeded)
        pass
