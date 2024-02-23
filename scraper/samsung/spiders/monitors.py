import scrapy


class MonitorsSpider(scrapy.Spider):
    name = "monitors"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/monitors/all-monitors/"]

    def parse(self, response):
        pass
