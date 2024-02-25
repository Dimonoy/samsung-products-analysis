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
        standard_price = None
        currency = None
        member_price = None
        benefit_price = None
        outlet_special_price = None
        coupon_discount_quantity = None
        coupon_discount_price = None

        extract_quantity = lambda pb: pb.css("dd span::text").get().strip()

        for price_block in response.css("itm-price dl").getall():
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

        return {
            "title": response.css("#goodsDetailNm::text").get(),
            "model": response.css("div.itm-sku::text").get(),
            "category": self.name,
            "standard_price": standard_price,
            "currency": currency,
            "member_price": member_price,
            "discount_quantity": response.css().get(),
            "benefit_price": benefit_price,
            "benefit_price_validity_period": response.css().get(),
            "coupon_discount_quantity": coupon_discount_quantity,
            "coupon_discount_period": response.css().get(),
            "coupon_discounted_price": coupon_discount_price,
            "outlet_special_price": outlet_special_price,
            "rating": response.css("itm-sart-rating span::text").get(),
            "quantity_of_reviews": response.css("itm-review-count::text").get(),
            "additional_properties": { k: v for k, v in response.css("").getall() },
        }
