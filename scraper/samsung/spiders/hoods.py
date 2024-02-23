import scrapy


class HoodsSpider(scrapy.Spider):
    name = "hoods"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/hood/all-hood/"]

    def parse(self, response):
        pass
