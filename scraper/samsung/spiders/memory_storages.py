import scrapy


class MemoryStoragesSpider(scrapy.Spider):
    name = "memory_storages"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/memory-storage/all-memory-storage/"]

    def parse(self, response):
        pass
