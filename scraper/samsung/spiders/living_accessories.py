import scrapy


class LivingAccessoriesSpider(scrapy.Spider):
    name = "living_accessories"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/living-accessories/all-living-accessories/"]

    def parse(self, response):
        pass
