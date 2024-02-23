import scrapy


class SamsungAudiosSpider(scrapy.Spider):
    name = "samsung_audios"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/samsung-audio/all-samsung-audio/"]

    def parse(self, response):
        pass
