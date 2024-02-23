import scrapy


class VacuumCleanersSpider(scrapy.Spider):
    name = "vacuum_cleaners"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/air-cleaner/all-air-cleaner/"]

    def parse(self, response):
        pass
