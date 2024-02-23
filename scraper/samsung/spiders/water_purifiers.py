import scrapy


class WaterPurifiersSpider(scrapy.Spider):
    name = "water_purifiers"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/water-purifier/all-water-purifier/"]

    def parse(self, response):
        pass
