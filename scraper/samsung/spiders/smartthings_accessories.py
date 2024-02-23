import scrapy


class SmartthingsAccessoriesSpider(scrapy.Spider):
    name = "smartthings_accessories"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/smartthings-accessories/all-smartthings-accessories/"]

    def parse(self, response):
        pass
