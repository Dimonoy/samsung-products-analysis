import scrapy


class AirdressersSpider(scrapy.Spider):
    name = "airdressers"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/airdresser/all-airdresser/"]

    def parse(self, response):
        pass
