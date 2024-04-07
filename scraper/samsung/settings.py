import pathlib
import os

from dotenv import load_dotenv


load_dotenv()

BOT_NAME = "samsung"

SPIDER_MODULES = ["samsung.spiders"]
NEWSPIDER_MODULE = "samsung.spiders"

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 4
DOWNLOAD_DELAY = 2

HTTPCACHE_ENABLED = True
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_POLICY = "scrapy.extensions.httpcache.RFC2616Policy"
HTTPCACHE_GZIP = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    "samsung.pipelines.PricesPipeline": 300,
    "samsung.pipelines.MySQLPipeline": 900,
}

MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_TABLE = os.getenv("MYSQL_TABLE")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
