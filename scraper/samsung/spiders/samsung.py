import scrapy
import json

from scrapy.loader import ItemLoader
from datetime import datetime
from dataclasses import dataclass

from typing import Literal

from ..items import SamsungProductItem


CLASSIFICATION_NUMBERS = (
    33010000, 33020000, 39120000, 33110000, 33120000, 33050000, 34060000,
    34080000, 41040000, 41090000, 34090000, 36010000, 36020000, 36080000,
    36070000, 36030000, 36060000, 37020000, 37080000, 37090000, 37010000,
    37040000, 37030000, 37050000, 37070000, 39020000, 39060000, 39030000,
    39040000, 39070000, 40030000, 100020195, 100034611, 100027453,
    100037843, 100020234, 100024278,
)
URL_ENDPOINT = "https://www.samsung.com/sec/pf/goodsList"
URL_PREFIX = "https://www.samsung.com/sec/"


@dataclass(eq=False)
class URLEndpointParameters:
    dispClsfNo: str
    pfFasterUseYn: Literal["Y", "N"] = "Y"
    page: int = 1
    rows: int = 25535
    secApp: bool = False
    ehcacheYn: Literal["Y", "N"] = "Y"
    soldOutExceptYn: Literal["Y", "N"] = "N"


class SamsungSpider(scrapy.Spider):
    name = "samsung"
    allowed_domains = ["www.samsung.com"]

    def start_requests(self):
        from scrapy.utils.url import add_or_replace_parameters
        from dataclasses import asdict

        for classification_number in CLASSIFICATION_NUMBERS:
            parameters = URLEndpointParameters(
                dispClsfNo=classification_number
            )
            url = add_or_replace_parameters(url=URL_ENDPOINT,
                                            new_parameters=asdict(parameters))

            yield scrapy.Request(url=url,
                                 callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        response_json = json.loads(response.body)

        for item in response_json["products"]:
            item_loader = ItemLoader(item=SamsungProductItem())
            prices = item.get("priceStr")

            if item.get("activatePhoneYn") == "Y":
                item_loader.add_value(
                    "prices",
                    "|".join(item.get("priceStr").split + ["activatePhoneY"])
                )
            elif item.get("outletFlgYn") == "Y":
                item_loader.add_value(
                    "prices",
                    "|".join(prices.split("|") + ["outletFlgY"])
                )

            item_loader.add_value("prices",
                                  prices)
            item_loader.add_value("title",
                                  item.get("goodsNm"))
            item_loader.add_value("model",
                                  item.get("mdlNm"))
            item_loader.add_value("model_code",
                                  item.get("mdlCode"))
            item_loader.add_value("link",
                                  URL_PREFIX + item.get("goodsDetailUrl"))
            item_loader.add_value("item_category",
                                  item.get("compDispClsfEnNm"))
            item_loader.add_value("item_classification_number",
                                  item.get("compDispClsfNo"))
            item_loader.add_value("rating",
                                  item.get("reviewGrade"))
            item_loader.add_value("quantity_of_reviews",
                                  item.get("reviewCount"))
            item_loader.add_value("stock_quantity",
                                  item.get("stockQty"),)
            item_loader.add_value("date_time_collected",
                                  datetime.now().isoformat())
            item_loader.add_value("coupon_discount",
                                  item.get("cpAllDcAmt"))
            item_loader.add_value("additional_properties",
                                  item.get("goodsOptStr"))

            yield item_loader.load_item()
