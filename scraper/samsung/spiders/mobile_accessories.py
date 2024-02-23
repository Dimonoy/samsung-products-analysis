import scrapy


class MobileAccessoriesSpider(scrapy.Spider):
    name = "mobile_accessories"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/mobile-accessories/all-mobile-accessories/"]

    def parse(self, response):
        pass
