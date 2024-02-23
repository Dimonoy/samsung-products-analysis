import scrapy


class TabletsSpider(scrapy.Spider):
    name = "tablets"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/tablets/all-tablets/"]

    def parse(self, response):
        pass
