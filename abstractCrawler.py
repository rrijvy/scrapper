from abc import ABC, abstractmethod


class AbstractCrawler(ABC):
    @abstractmethod
    def startCrawl(self) -> bool:
        pass
