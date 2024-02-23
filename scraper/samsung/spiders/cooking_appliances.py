import scrapy


class CookingAppliancesSpider(scrapy.Spider):
    name = "cooking_appliances"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/cooking-appliances/all-cooking-appliances/"]

    def parse(self, response):
        pass
