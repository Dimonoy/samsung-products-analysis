import scrapy


class WashingMachinesSpider(scrapy.Spider):
    name = "washing_machines"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/washing-machines/all-washing-machines/"]

    def parse(self, response):
        pass
