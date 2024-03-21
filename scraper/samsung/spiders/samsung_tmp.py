import scrapy
import json

from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Literal


CLASSIFICATION_NUMBERS = (
    # 33010000, 33020000, 39120000, 33110000, 33120000, 33050000, 34060000, 34080000,
    # 41040000, 41090000, 34090000, 36010000, 36020000, 36080000, 36070000, 36030000,
    # 36060000, 37020000, 37080000, 37090000, 37010000, 37040000, 37030000, 37050000,
    # 37070000, 39020000, 39060000, 39030000, 39040000, 39070000, 40030000,
    # 100020195, 100034611, 100027453, 100037843, 100020234, 100024278,
    33010000,
)
URL_ENDPOINT = "https://www.samsung.com/sec/pf/goodsList"
URL_PREFIX = "https://www.samsung.com/sec/"
DATETIME_FORMAT = "%Y/%d/%m %H:%M:%S"


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
    name = "samsung_tmp"
    allowed_domains = ["www.samsung.com"]

    def start_requests(self):
        from scrapy.utils.url import add_or_replace_parameters

        for classification_number in CLASSIFICATION_NUMBERS:
            parameters = URLEndpointParameters(dispClsfNo=classification_number)
            url = add_or_replace_parameters(
                url=URL_ENDPOINT,
                new_parameters=asdict(parameters),
            )

            yield scrapy.Request(
                url=url,
                callback=self.parse,
            )

    def parse(self, response: scrapy.http.Response):
        response_json = json.loads(response.body)
        self.log(response_json)

        for item in response_json["products"]:
            has_outlet = False
            prices = None
            additional_properties = None

            if item.get("activatePhoneYn") == "Y":
                prices = get_prices_schema()
            if item.get("outletFlgYn") == "Y":
                has_outlet = True
            if prices is None:
                prices = deserialize_price_string(item.get("priceStr"), has_outlet=has_outlet)

            addtional_properties = deserialize_additional_properties_string(
                item.get("goodsOptStr")
            )

            yield {
                "title": item.get("goodsNm"),
                "model": item.get("mdlNm"),
                "model_code": item.get("mdlCode"),
                "link": URL_PREFIX + item.get("goodsDetailUrl"),
                "item_category": item.get("compDispClsfEnNm"),
                "item_classification_number": item.get("compDispClsfNo"),
                "rating": item.get("reviewGrade"),
                "reviews_quantity": item.get("reviewCount"),
                "stock_quantity": item.get("stockQty"), 
                "datetime": datetime.now().strftime(DATETIME_FORMAT),
                "coupon_discount": item.get("cpAllDcAmt"),
                "additional_properties": addtional_properties,
                **prices,
            }


def get_prices_schema():
    return {
        "standard_price": None,
        "member_price": None,
        "benefit_price": None,
        "outlet_special_price": None,
    }


def deserialize_price_string(price_split: str, has_outlet: bool):
    price_split = price_split.split("|")
    prices_schema = get_prices_schema()

    price_split[2], price_split[3] = int(price_split[2]), int(price_split[3])
    prices_schema["standard_price"] = price_split[2]

    if has_outlet:
        prices_schema["outlet_special_price"] = int(price_split[-1])
    elif price_split[1] == '00':
        prices_schema["member_price"] = price_split[3] if price_split[2] != price_split[3] else None
    elif price_split[1] != '00':
        price_split[4] = int(price_split[4])

        if price_split[2] == price_split[3] and price_split[3] != price_split[4]:
            prices_schema["benefit_price"] = price_split[4]
        elif price_split[2] != price_split[3] and price_split[3] != price_split[4]:
            prices_schema["member_price"] = price_split[3]
            prices_schema["benefit_price"] = price_split[4]


    return prices_schema


def deserialize_additional_properties_string(additional_properties_str: str):
    if additional_properties_str is None:
        return additional_properties_str

    additional_properties_split = additional_properties_str.split("\n")
    additional_properties_schema = {}

    for property in additional_properties_split:
        property_split = property.split("|")
        property_key = property_split[-3]
        property_value = property_split[-2]

        if additional_properties_schema.get(property_key):
            additional_properties_schema[property_key].append(property_value)
        else:
            additional_properties_schema[property_key] = [property_value]

    return additional_properties_schema
