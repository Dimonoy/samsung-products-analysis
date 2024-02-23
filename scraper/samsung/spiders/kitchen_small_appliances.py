import scrapy


class KitchenSmallAppliancesSpider(scrapy.Spider):
    name = "kitchen_small_appliances"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/kitchen-small-appliance/all-kitchen-small-appliance/"]

    def parse(self, response):
        pass
