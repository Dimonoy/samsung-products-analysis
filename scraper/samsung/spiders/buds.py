import scrapy


class BudsSpider(scrapy.Spider):
    name = "buds"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/buds/all-buds/"]

    def parse(self, response):
        pass
