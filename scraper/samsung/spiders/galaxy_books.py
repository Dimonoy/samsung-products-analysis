import scrapy


class GalaxyBooksSpider(scrapy.Spider):
    name = "galaxy_books"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/galaxybook/all-galaxybook/"]

    def parse(self, response):
        pass
