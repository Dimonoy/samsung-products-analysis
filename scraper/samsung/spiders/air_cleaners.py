import scrapy


class AirCleanersSpider(scrapy.Spider):
    name = "air_cleaners"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/air-cleaner/all-air-cleaner/"]

    def parse(self, response):
        pass
