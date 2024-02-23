import scrapy


class AirConditionersSpider(scrapy.Spider):
    name = "air_conditioners"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/air-conditioners/all-air-conditioners/"]

    def parse(self, response):
        pass
