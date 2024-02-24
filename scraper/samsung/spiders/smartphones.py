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
        return {
            "title": response.css("#goodsDetailNm::text").get(),
            "model": response.css("div.itm-sku::text").get(),
            "category": self.name,
            "standard_price": response.css("#originalPrice").attrib["value"],
            "member_price": response.css().get(),
            "discount_quantity": response.css().get(),
            "benefit_price": response.css().get(),
            "benefit_price_validity_period": response.css().get(),
            "coupon_discount_quantity": response.css().get(),
            "coupon_discount_period": response.css().get(),
            "coupon_discounted_price": response.css().get(),
            "event_price": response.css().get(),
            "rating": response.css("itm-sart-rating span::text").get(),
            "quantity_of_reviews": response.css("itm-review-count::text").get(),
            "additional_properties": { k: v for k, v in response.css("").getall() },
        }
