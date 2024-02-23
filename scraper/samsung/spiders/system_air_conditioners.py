import scrapy


class SystemAirConditionersSpider(scrapy.Spider):
    name = "system_air_conditioners"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/system-air-conditioners/all-system-air-conditioners/"]

    def parse(self, response):
        pass
