import scrapy


class MicrowaveOvensSpider(scrapy.Spider):
    name = "microwave_ovens"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/micro-wave-ovens/all-micro-wave-ovens/"]

    def parse(self, response):
        pass
