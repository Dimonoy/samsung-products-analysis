from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


if __name__ == '__main__':
    process = CrawlerProcess(settings=get_project_settings())

    process.crawl(crawler_or_spidercls="samsung")
    process.start()
