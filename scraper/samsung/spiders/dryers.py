import scrapy


class DryersSpider(scrapy.Spider):
    name = "dryers"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/dryers/all-dryers/"]

    def parse(self, response):
        pass
