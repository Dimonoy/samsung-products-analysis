import scrapy
from playwright.async_api import Page


class SamsungSpider(scrapy.Spider):
    name = "samsung_tmp"
    allowed_domains = ["www.samsung.com"]
    start_urls = [
	    # "https://www.samsung.com/sec/smartphones/all-smartphones/",
	    # "https://www.samsung.com/sec/tablets/all-tablets/",
	    # "https://www.samsung.com/sec/water-purifier/all-water-purifier/",
	    # "https://www.samsung.com/sec/electric-range/all-electric-range/",
	    # "https://www.samsung.com/sec/kitchen-small-appliance/all-kitchen-small-appliance/",
	    # "https://www.samsung.com/sec/washing-machines/all-washing-machines/",
	    "https://www.samsung.com/sec/dryers/all-dryers/",
	    # "https://www.samsung.com/sec/airdresser/all-airdresser/",
	    # "https://www.samsung.com/sec/air-conditioners/all-air-conditioners/",
	    # "https://www.samsung.com/sec/smartthings-accessories/all-smartthings-accessories/",
    ]

    def start_requests(self):
        for products_list_url in self.start_urls:
            yield scrapy.Request(
                url=products_list_url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    # "playwright_context": "product_lists",
                },
                callback=self.parse,
            )

    async def load_all_items(self, page: Page):
        from lxml.etree import HTMLParser, fromstring as html_from_string

        await page.wait_for_selector("button#morePrd")
        amount_of_sets = int(await page.locator("span#totalPageCount").text_content())
        
        item_number = 11
        for _ in range(amount_of_sets):
            await page.wait_for_selector(f"li.item:nth-child({item_number})")
            await page.evaluate("morePrd()")
            item_number += 12

        html = html_from_string(await page.locator("ul.list-type").inner_html(), HTMLParser())

        await page.close()
        await page.context.close()

        return html, amount_of_sets
       
    async def parse(self, response: scrapy.http.Response):
        html, amount_of_sets = await self.load_all_items(response.meta["playwright_page"])

        for n, card_url_selector in enumerate(html.cssselect("li.item a.link-review"), start=1):
            card_url_postfix = card_url_selector.attrib["href"]
            card_url_postfix = card_url_postfix.rstrip("?focus=review")
            card_url = response.urljoin(card_url_postfix)

            context_number = n % amount_of_sets
            yield scrapy.Request(
                url=card_url,
                meta={ "playwright": True },
                callback=self.parse_card,
            )

    async def parse_card(self, response: scrapy.http.Response):
        prices_selector = response.css("div.itm-price")
        props_selector = response.css("div.itm-option-choice")

        return {
            "title": response.css("h1#goodsDetailNm::text").get(),
            "url": response.url,
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
            self.log(price_selector.css("dt::text").get().strip())
            match price_selector.css("dt::text").get().strip():
                case "기준가":
                    prices["standard_price"] = extract_quantity(price_selector)
                case "회원가":
                    prices["member_price"] = extract_quantity(price_selector)
                case "혜택가":
                    prices["benefit_price"] = extract_quantity(price_selector)
                case "아울렛 특가":
                    prices["outlet_special_price"] = extract_quantity(price_selector)
                case "쿠폰 할인 금액":
                    prices["coupon_discount_quantity"] = extract_quantity(price_selector)
                case "쿠폰 적용 예상가":
                    prices["coupon_discounted_price"] = extract_quantity(price_selector)
                case other:
                    self.logger.warn(f"'{other}' is not defined by the parser")

        return prices

    def parse_additional_props(self, props_selector: scrapy.Selector):
        props = {}

        for prop_selector in props_selector.css("dl")[:-1]:
            if prop_selector.attrib["class"] not in ("count-show-box", "itm-option-etc"):
                prop_title = prop_selector.css("dt span::text").get()
                prop_values = prop_selector.css("dd li span::text").getall()

                props[prop_title] = prop_values

        return props
