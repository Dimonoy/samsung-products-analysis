import scrapy


class KitchenAccessoriesSpider(scrapy.Spider):
    name = "kitchen_accessories"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/kitchen-accessories/all-kitchen-accessories/"]

    def parse(self, response):
        pass
