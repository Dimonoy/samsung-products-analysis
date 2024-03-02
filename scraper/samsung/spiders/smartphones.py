import scrapy


class SmartphonesSpider(scrapy.Spider):
    name = "smartphones"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/sec/smartphones/all-smartphones/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                meta={ "playwright": True },
            )
       

    def parse(self, response: scrapy.http.Response):
        for card in response.css("li.item"):
            card_url_postfix = card.css("a.link-review").attrib["href"]
            card_url_postfix = card_url_postfix.rstrip("?focus=review")
            url = response.urljoin(card_url_postfix)

            yield scrapy.Request(
                url=url,
                meta={ "playwright": True },
                callback=self.parse_card,
            )

    async def parse_card(self, response: scrapy.http.Response):
        prices_selector = response.css("div.itm-price")[0]
        props_selector = response.css("div.itm-option-choice")[0]
        self.log("Parsing a card .............................................")

        return {
            "title": response.css("h1#goodsDetailNm::text").get(),
            "model": response.css("div.itm-sku::text").get(),
            "category": self.name,

            # "benefit_price_validity_period": response.css().get(),
            # "coupon_discount_validity_period": response.css().get(),

            "rating": response.css("div.itm-sart-rating span::text").get(),
            "quantity_of_reviews": response.css("a.itm-review-count::text").get(),
            **self.parse_prices(prices_selector),
            **self.parse_additional_props(props_selector),
        }

    def parse_prices(self, prices_selector: scrapy.Selector):
        prices = {
            "standard_price": None,
            "member_price": None,
            "benefit_price": None,
            "outlet_special_price": None,
            "coupon_discount_quantity": None,
            "coupon_discounted_price": None,
        }
        extract_quantity = lambda pb: pb.css("dd span::text").get().strip()

        for price_selector in prices_selector.css("dl"):
            match price_selector.css("dt::text").get().strip():
                case "기준가":
                    standard_price = extract_quantity(price_selector)
                case "회원가":
                    member_price = extract_quantity(price_selector)
                case "혜택가":
                    benefit_price = extract_quantity(price_selector)
                case "아울렛 특가":
                    outlet_special_price = extract_quantity(price_selector)
                case "쿠폰 할인 금액":
                    coupon_discount_quantity = extract_quantity(price_selector)
                case "쿠폰 적용 예상가":
                    coupon_discounted_price = extract_quantity(price_selector)
                case other:
                    self.logger.warn(f"'{other}' is not defined by the parser")

        self.log(prices)
        return prices

    def parse_additional_props(self, props_selector: scrapy.Selector):
        props = {}

        for prop_selector in props_selector.css("dl")[:-1]:
            if prop_selector.attrib["class"] not in ("count-show-box", "itm-option-etc"):
                prop_title = prop_selector.css("dt span::text").get()
                prop_values = prop_selector.css("dd li span::text").getall()

                props[prop_title] = prop_values

        self.log(props)
        return props
