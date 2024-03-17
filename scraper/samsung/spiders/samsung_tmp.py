import scrapy
import json


class SamsungSpider(scrapy.Spider):
    name = "samsung_tmp"
    allowed_domains = ["www.samsung.com"]
    tmp_url_prefix = "https://www.samsung.com/sec/"
    template_url = "https://www.samsung.com/sec/pf/goodsList?dispClsfNo={}&page=1&rows=1&ehcacheYn=Y&soldOutExceptYn=N&pfFasterUseYn=Y&secApp=false"
    category_to_classification_number = {
        "all-smartphones":             33010000,
        "all-tablets":                 33020000,
        "all-galaxybook":              39120000,
        "all-watches":                 33110000,
        "all-buds":                    33120000,
        "all-mobile-accessories":      33050000,
        "all-tvs":                     34060000,
        "all-lifestyletv":             34080000,
        "all-samsung-audio":           41040000,
        "all-harman-life-style-audio": 41090000,
        "all-tv-accessories":          34090000,
        "all-refrigerators":           36010000,
        "all-kimchi-refrigerators":    36020000,
        "all-dishwashers":             36080000,
        "all-water-purifier":          100020195,
        "all-electric-range":          36070000,
        "all-cooking-appliances":      36030000,
        "all-micro-wave-ovens":        100034611,
        "all-hood":                    100027453,
        "all-kitchen-small-appliance": 100037843,
        "all-kitchen-accessories":     36060000,
        "all-washing-machines":        37020000,
        "all-dryers":                  37080000,
        "all-airdresser":              37090000,
        "all-shoedresser":             100020234,
        "all-air-conditioners":        37010000,
        "all-system-air-conditioners": 100024278,
        "all-air-cleaner":             37040000,
        "all-vacuum-cleaners":         37030000,
        "all-small-appliances":        37050000,
        "all-living-accessories":      37070000,
        "all-desktop":                 39020000,
        "all-pc-accessories":          39060000,
        "all-monitors":                39030000,
        "all-printers":                39040000,
        "all-printer-supplies":        39070000,
        "all-memory-storage":          40030000,
        "all-smartthings-accessories": 100024735,
    }

    def start_requests(self):
        for product_category, classification_number in self.category_to_classification_number.items():
            self.start_urls.append(self.template_url.format(classification_number))

            yield scrapy.Request(
                url=self.start_urls[-1],
                meta={ 'product-category': product_category },
                callback=self.parse,
            )

    def parse(self, response: scrapy.http.Response):
        response_json = json.loads(response.body)
        response_json = response_json.get('products')[0]
        new_json = {}

        for key, value in response_json.items():
            if value is None:
                continue
            elif type(value) == dict:
                new_json1 = {}
                for key1, value1 in value.items():
                    if value1 is None:
                        continue
                    else:
                        pass
                        new_json1.update({key1: value1})
                new_json.update({key: new_json1})
            else:
                new_json.update({key: value})

        yield new_json
    # async def parse(self, response: scrapy.http.Response):
    #     html, amount_of_sets = await self.load_all_items(response.meta["playwright_page"])

    #     for n, card_url_selector in enumerate(html.cssselect("li.item a.link-review"), start=1):
    #         card_url_postfix = card_url_selector.attrib["href"]
    #         card_url_postfix = card_url_postfix.rstrip("?focus=review")
    #         card_url = response.urljoin(card_url_postfix)

    #         context_number = n % amount_of_sets
    #         yield scrapy.Request(
    #             url=card_url,
    #             meta={ "playwright": True },
    #             callback=self.parse_card,
    #         )

    # async def parse_card(self, response: scrapy.http.Response):
    #     prices_selector = response.css("div.itm-price")
    #     props_selector = response.css("div.itm-option-choice")

    #     return {
    #         "title": response.css("h1#goodsDetailNm::text").get(),
    #         "url": response.url,
    #         "model": response.css("div.itm-sku::text").get(),
    #         "category": self.name,

    #         # "benefit_price_validity_period": response.css().get(),
    #         # "coupon_discount_validity_period": response.css().get(),

    #         "rating": response.css("div.itm-sart-rating span::text").get(),
    #         "quantity_of_reviews": response.css("a.itm-review-count::text").get(),
    #         **self.parse_prices(prices_selector),
    #         **self.parse_additional_props(props_selector),
    #     }

    # def parse_prices(self, prices_selector: scrapy.Selector):
    #     prices = {
    #         "standard_price": None,
    #         "member_price": None,
    #         "benefit_price": None,
    #         "outlet_special_price": None,
    #         "coupon_discount_quantity": None,
    #         "coupon_discounted_price": None,
    #     }
    #     extract_quantity = lambda pb: pb.css("dd span::text").get().strip()

    #     for price_selector in prices_selector.css("dl"):
    #         self.log(price_selector.css("dt::text").get().strip())
    #         match price_selector.css("dt::text").get().strip():
    #             case "기준가":
    #                 prices["standard_price"] = extract_quantity(price_selector)
    #             case "회원가":
    #                 prices["member_price"] = extract_quantity(price_selector)
    #             case "혜택가":
    #                 prices["benefit_price"] = extract_quantity(price_selector)
    #             case "아울렛 특가":
    #                 prices["outlet_special_price"] = extract_quantity(price_selector)
    #             case "쿠폰 할인 금액":
    #                 prices["coupon_discount_quantity"] = extract_quantity(price_selector)
    #             case "쿠폰 적용 예상가":
    #                 prices["coupon_discounted_price"] = extract_quantity(price_selector)
    #             case other:
    #                 self.logger.warn(f"'{other}' is not defined by the parser")

    #     return prices

    # def parse_additional_props(self, props_selector: scrapy.Selector):
    #     props = {}

    #     for prop_selector in props_selector.css("dl")[:-1]:
    #         if prop_selector.attrib["class"] not in ("count-show-box", "itm-option-etc"):
    #             prop_title = prop_selector.css("dt span::text").get()
    #             prop_values = prop_selector.css("dd li span::text").getall()

    #             props[prop_title] = prop_values

    #     return props
