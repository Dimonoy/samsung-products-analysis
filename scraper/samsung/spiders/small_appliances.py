import scrapy


class SmallAppliancesSpider(scrapy.Spider):
    name = "small_appliances"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/small-appliances/all-small-appliances/"]

    def parse(self, response):
        pass
