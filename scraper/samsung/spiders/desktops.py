import scrapy


class DesktopsSpider(scrapy.Spider):
    name = "desktops"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/desktop/all-desktop/"]

    def parse(self, response):
        pass
