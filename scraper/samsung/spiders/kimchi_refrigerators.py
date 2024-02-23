import scrapy


class KimchiRefrigeratorsSpider(scrapy.Spider):
    name = "kimchi_refrigerators"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/kimchi-refrigerators/all-kimchi-refrigerators/"]

    def parse(self, response):
        pass
