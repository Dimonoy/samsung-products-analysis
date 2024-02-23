import scrapy


class TvsSpider(scrapy.Spider):
    name = "tvs"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/tvs/all-tvs/"]

    def parse(self, response):
        pass
