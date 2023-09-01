from requests import Response
from abstractCrawler import AbstractCrawler


class AmazonCrawler(AbstractCrawler):
    def startCrawl(self, response: Response) -> bool:
        print("Amazon crawling")
        return True
