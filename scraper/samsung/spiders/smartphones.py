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
            card_url_postfix = card.css("link-review").attrib["href"]
            card_url_postfix = card_url_postfix.rstrip("?focus=review")
            url = response.urljoin(card_url_postfix)

            yield response.follow(
                url=url,
                callback=self.parse_card,
            )

    def parse_card(self, response: scrapy.http.Response):
        item = None
        prices_selector = response.css("itm-price")
        props_selector = response.css("itm-option-choice")

        return {
            "title": response.css("#goodsDetailNm::text").get(),
            "model": response.css("div.itm-sku::text").get(),
            "category": self.name,

            "benefit_price_validity_period": response.css().get(),
            "coupon_discount_validity_period": response.css().get(),

            "rating": response.css("itm-sart-rating span::text").get(),
            "quantity_of_reviews": response.css("itm-review-count::text").get(),
            **self.parse_prices(prices_selector),
            **self.parse_additional_props(props_selector),
        }

    def parse_prices(prices_selector: scrapy.Selector):
        prices = {
            "standard_price": None,
            "member_price": None,
            "benefit_price": None,
            "outlet_special_price": None,
            "coupon_discount_quantity": None,
            "coupon_discounted_price": None,
        }
        extract_quantity = lambda pb: pb.css("dd span::text").get().strip()

        for price_block in prices_selector.css("dl"):
            match price_block.css("dt::text").get().strip():
                case "기준가":
                    standard_price = extract_quantity(price_block)
                case "회원가":
                    member_price = extract_quantity(price_block)
                case "혜택가":
                    benefit_price = extract_quantity(price_block)
                case "아울렛 특가":
                    outlet_special_price = extract_quantity(price_block)
                case "쿠폰 할인 금액":
                    coupon_discount_quantity = extract_quantity(price_block)
                case "쿠폰 적용 예상가":
                    coupon_discounted_price = extract_quantity(price_block)
                case other:
                    self.logger.warn(f"'{other}' is not defined by the parser")

    def parse_additional_props(props_selector: scrapy.Selector):
        pass
