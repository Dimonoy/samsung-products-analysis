import scrapy


class SmartphonesSpider(scrapy.Spider):
    name = "smartphones"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/smartphones/all-smartphones/"]

    def parse(self, response):
        pass
