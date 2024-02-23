import scrapy


class RefrigeratorsSpider(scrapy.Spider):
    name = "refrigerators"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/refrigerators/all-refrigerators/"]

    def parse(self, response):
        pass
