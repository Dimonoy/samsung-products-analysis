import scrapy


class GalaxybooksSpider(scrapy.Spider):
    name = "galaxybooks"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/galaxybook/all-galaxybook/"]

    def parse(self, response):
        pass
