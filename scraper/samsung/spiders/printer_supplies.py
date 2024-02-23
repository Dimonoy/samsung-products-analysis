import scrapy


class PrinterSuppliesSpider(scrapy.Spider):
    name = "printer_supplies"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/printer-supplies/all-printer-supplies/"]

    def parse(self, response):
        pass
