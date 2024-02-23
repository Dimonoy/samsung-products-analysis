import scrapy


class PcAccessoriesSpider(scrapy.Spider):
    name = "pc_accessories"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/pc-accessories/all-pc-accessories/"]

    def parse(self, response):
        pass
