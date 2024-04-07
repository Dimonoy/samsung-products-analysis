from scrapy.crawler import Crawler

import mysql.connector

from itemadapter import ItemAdapter
from samsung.items import SamsungProductItem
from samsung.spiders.samsung import SamsungSpider
from logging import ERROR


class PricesPipeline:
    def process_item(self, item, spider):
        item_ = ItemAdapter(item)

        item_["standard_price"] = item_.get("prices").get("standard")
        item_["member_price"] = item_.get("prices").get("member")
        item_["benefit_price"] = item_.get("prices").get("benefit")
        item_["outlet_special_price"] = item_.get("prices")\
                                             .get("outlet_special")

        item_.pop("prices")

        return item_.item


class MySQLPipeline:
    username = None
    password = None
    database = None
    table = None
    host = None
    port = None
    db_client = None
    add_record_query = None

    def __init__(self, username: str, password: str,
                 database: str, host: str, port: int,
                 table: str):
        self.username = username
        self.password = password
        self.database = database
        self.host = host
        self.port = port

        columns = ("title", "model", "model_code", "link", "item_category",
                   "item_classification_number", "rating",
                   "quantity_of_reviews", "stock_quantity",
                   "additional_properties", "date_time_collected",
                   "standard_price", "member_price", "benefit_price",
                   "coupon_discount", "outlet_special_price")
        values = (f"%({value})s" for value in columns)

        self.add_record_query = \
            (f"INSERT INTO {table}({', '.join(columns)}) "
             f"VALUES ({', '.join(values)})")

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls(
            username=crawler.settings.get("MYSQL_USERNAME"),
            password=crawler.settings.get("MYSQL_PASSWORD"),
            database=crawler.settings.get("MYSQL_DATABASE"),
            table=crawler.settings.get("MYSQL_TABLE"),
            host=crawler.settings.get("MYSQL_HOST"),
            port=crawler.settings.get("MYSQL_PORT"),
        )

    def open_spider(self, spider: SamsungSpider):
        self.db_client = mysql.connector.connect(
            user=self.username,
            password=self.password,
            host=self.host,
            database=self.database,
            port=self.port,
        )

    def close_spider(self, spider: SamsungSpider):
        self.db_client.close()

    def process_item(self, item: SamsungProductItem, spider: SamsungSpider):
        assert self.db_client.is_connected(), \
        "[ERROR] MySQL database connection has not been established!"

        item_dict = ItemAdapter(item).asdict()

        with self.db_client.cursor() as cursor:
            cursor.execute(self.add_record_query,
                           item_dict)
            self.db_client.commit()
            cursor.close()

        return item
