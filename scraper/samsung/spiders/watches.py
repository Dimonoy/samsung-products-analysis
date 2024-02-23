import scrapy


class WatchesSpider(scrapy.Spider):
    name = "watches"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/watches/all-watches/"]

    def parse(self, response):
        pass
