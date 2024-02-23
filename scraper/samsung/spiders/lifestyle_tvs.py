import scrapy


class LifestyleTvsSpider(scrapy.Spider):
    name = "lifestyle_tvs"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/lifestyletv/all-lifestyletv/"]

    def parse(self, response):
        pass
