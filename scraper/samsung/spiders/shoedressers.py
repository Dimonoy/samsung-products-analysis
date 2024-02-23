import scrapy


class ShoedressersSpider(scrapy.Spider):
    name = "shoedressers"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/shoedresser/all-shoedresser/"]

    def parse(self, response):
        pass
