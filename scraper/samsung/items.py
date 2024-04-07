import scrapy
import json

from typing import Literal
from typing_extensions import Self
from itemloaders.processors import TakeFirst


class PricesItem(scrapy.Item):
    standard = scrapy.Field(output_processor=TakeFirst())
    member = scrapy.Field(output_processor=TakeFirst())
    benefit = scrapy.Field(output_processor=TakeFirst())
    outlet_special = scrapy.Field(output_processor=TakeFirst())

    def get_defaults() -> Self:
        return PricesItem(
            standard=None,
            member=None,
            benefit=None,
            outlet_special=None,
        )


class Deserialize:
    def __init__(self, target=Literal['prices', 'add_props']) -> None:
        assert target in ('prices', 'add_props'), f"""
            `Deserialize` class expects `target` to be set to \"prices\" or
            \"add_props\", not \"{target}\"
        """

        self.target = target

    def __call__(self, item_str: list[str | None]) -> None:
        item_str = item_str[0]

        if self.target == "prices":
            self.prices_from_str(item_str)
        if self.target == "add_props":
            self.add_props_from_str(item_str)

    @staticmethod
    def prices_from_str(price_str: str) -> dict[str, int]:
        prices = price_str.split("|")
        prices_item = PricesItem.get_defaults()

        for i, price in enumerate(prices):
            prices[i] = int(price) if price.isdigit() else price

        if prices[-1] == "activatePhoneY" or prices[2] == 0:
            return prices_item

        prices_item["standard"] = prices[2]

        if prices[-1] == "outletFlgY":
            prices_item["outlet_special"] = prices[-2]
        elif prices[1] == 0 and prices[2] != prices[3]:
            prices_item["member"] = prices[3]
        elif prices[1] != 0:
            if prices[2] == prices[3] and prices[3] != prices[4]:
                prices_item["benefit"] = prices[4]
            elif prices[2] != prices[3] and prices[3] != prices[4]:
                prices_item["member"] = prices[3]
                prices_item["benefit"] = prices[4]

        return dict(prices_item)

    @staticmethod
    def add_props_from_str(add_props_str: str | None) -> dict[str, list]:
        if add_props_str is None:
            return add_props_str

        add_props = add_props_str.split("\n")
        add_props_item = {}

        for prop in add_props:
            props = prop.split("|")
            prop_key = props[-3]
            prop_value = props[-2]

            if add_props_item.get(prop_key):
                add_props_item[prop_key].append(prop_value)
            else:
                add_props_item[prop_key] = [prop_value]

        return json.dumps(add_props_item)


class SamsungProductItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    model = scrapy.Field(output_processor=TakeFirst())
    model_code = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    item_category = scrapy.Field(output_processor=TakeFirst())
    item_classification_number = scrapy.Field(output_processor=TakeFirst())
    rating = scrapy.Field(output_processor=TakeFirst())
    quantity_of_reviews = scrapy.Field(output_processor=TakeFirst())
    stock_quantity = scrapy.Field(output_processor=TakeFirst())
    date_time_collected = scrapy.Field(output_processor=TakeFirst())
    coupon_discount = scrapy.Field(output_processor=TakeFirst())
    prices = scrapy.Field(
        input_processor=Deserialize(target='prices'),
        output_processor=TakeFirst(),
    )
    additional_properties = scrapy.Field(
        input_processor=Deserialize(target='add_props'),
        output_processor=TakeFirst(),
    )

    standard_price = scrapy.Field(output_processor=TakeFirst())
    member_price = scrapy.Field(output_processor=TakeFirst())
    benefit_price = scrapy.Field(output_processor=TakeFirst())
    outlet_special_price = scrapy.Field(output_processor=TakeFirst())
