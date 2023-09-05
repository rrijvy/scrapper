from io import StringIO
from requests import Response
from abstractCrawler import AbstractCrawler
from lxml import etree


class AmazonSearchCrawler(AbstractCrawler):
    def startCrawl(self, response: Response) -> bool:
        htmlParser = etree.HTMLParser()
        tree = etree.parse(StringIO(response.text), htmlParser)
        searchProductsElement = tree.xpath(
            '//*[@data-component-type="s-search-result" and @data-asin]'
        )
        for productElement in searchProductsElement:
            url = productElement.xpath(".//h2/a/@href")
            name = productElement.xpath(".//h2/a/span/text()")
            price = productElement.xpath(
                ".//*[contains(@class, 'a-price')]/span/text()"
            )
            print()

        print(searchProductsElement)
