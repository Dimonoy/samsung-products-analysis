import scrapy


class TvAccessoriesSpider(scrapy.Spider):
    name = "tv_accessories"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/tv-accessories/all-tv-accessories/"]

    def parse(self, response):
        pass
