import scrapy


class DishwashersSpider(scrapy.Spider):
    name = "dishwashers"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/dishwashers/all-dishwashers/"]

    def parse(self, response):
        pass
