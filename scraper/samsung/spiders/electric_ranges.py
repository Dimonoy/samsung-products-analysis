import scrapy


class ElectricRangesSpider(scrapy.Spider):
    name = "electric_ranges"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/electric-range/all-electric-range/"]

    def parse(self, response):
        pass
