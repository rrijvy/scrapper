from abc import ABC, abstractmethod
from requests import Response


class AbstractCrawler(ABC):
    @abstractmethod
    def startCrawl(self, response: Response) -> bool:
        
        pass
