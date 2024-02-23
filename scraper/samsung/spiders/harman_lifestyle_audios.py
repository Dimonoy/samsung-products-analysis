import scrapy


class HarmanLifestyleAudiosSpider(scrapy.Spider):
    name = "harman_lifestyle_audios"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/harman-life-style-audio/all-harman-life-style-audio/"]

    def parse(self, response):
        pass
