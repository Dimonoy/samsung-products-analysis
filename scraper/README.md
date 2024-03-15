# Samsung.com scraper
The scraper utilizes "concealed" samsung.com REST API, which is used during the product catalog webpages loading.  
The key takeaways from the samsung.com API:
- the Fetch/XHR request is performed by the client product catalog page and is unique;
- the request parameter to specify the product category is called "product classification number" ([See the table below](#product-categories));
- the response contains all the possible information for each product presented in the catalog;
- the request is easily adjustable to receive the desired amount of items and category.

## Product categories
There are in total 38 product categories presented on the https://www.samsung.com/sec/ (Korea) website. Product category names are taken 
from the product catalog URLs to those product categories. Each product classification number was manually collected from each page through the devtool.

| ID | Product category            | Product classification number | Korean name              |
|----|-----------------------------|-------------------------------|--------------------------|
| 1  | all-smartphones             | 33010000                      | 스마트폰                 |
| 2  | all-tablets                 | 33020000                      | 태블릿                   |
| 3  | all-galaxybook              | 39120000                      | 갤럭시북                 |
| 4  | all-watches                 | 33110000                      | 워치                     |
| 5  | all-buds                    | 33120000                      | 버즈                     |
| 6  | all-mobile-accessories      | 33050000                      | 모바일 액세서리          |
| 7  | all-tvs                     | 34060000                      | TV                       |
| 8  | all-lifestyletv             | 34080000                      | 라이프스타일 TV          |
| 9  | all-samsung-audio           | 41040000                      | 삼성 사운드바/뮤직프레임 |
| 10 | all-harman-life-style-audio | 41090000                      | JBL/하만카돈/마크레빈슨  |
| 11 | all-tv-accessories          | 34090000                      | TV & 오디오 엑세서리     |
| 12 | all-refrigerators           | 36010000                      | 냉장고                   |
| 13 | all-kimchi-refrigerators    | 36020000                      | 김치냉장고               |
| 14 | all-dishwashers             | 36080000                      | 식기세척기               |
| 15 | all-water-purifier          | 100020195                     | 정수기                   |
| 16 | all-electric-range          | 36070000                      | 전기레인지               |
| 17 | all-cooking-appliances      | 36030000                      | 큐커 멀티/오븐           |
| 18 | all-micro-wave-ovens        | 100034611                     | 전자레인지               |
| 19 | all-hood                    | 100027453                     | 후드                     |
| 20 | all-kitchen-small-appliance | 100037843                     | 주방가전 소형가전        |
| 21 | all-kitchen-accessories     | 36060000                      | 주방가전 액세서리        |
| 22 | all-washing-machines        | 37020000                      | 세탁기                   |
| 23 | all-dryers                  | 37080000                      | 건조기                   |
| 24 | all-airdresser              | 37090000                      | 에어드레서               |
| 25 | all-shoedresser             | 100020234                     | 슈드레서                 |
| 26 | all-air-conditioners        | 37010000                      | 에어컨                   |
| 27 | all-system-air-conditioners | 100024278                     | 시스템에어컨             |
| 28 | all-air-cleaner             | 37040000                      | 공기청정기/제습기        |
| 29 | all-vacuum-cleaners         | 37030000                      | 청소기                   |
| 30 | all-small-appliances        | 37050000                      | 리빙가전 소형가전        |
| 31 | all-living-accessories      | 37070000                      | 리빙가전 액세서리        |
| 32 | all-desktop                 | 39020000                      | 데스크탑                 |
| 33 | all-pc-accessories          | 39060000                      | PC 액세서리              |
| 34 | all-monitors                | 39030000                      | 모니터                   |
| 35 | all-printers                | 39040000                      | 프린터                   |
| 36 | all-printer-supplies        | 39070000                      | 토너/잉크                |
| 37 | all-memory-storage          | 40030000                      | 메모리/스트리지          |
| 38 | all-smartthings-accessories | 100024735                     | 스마트싱스 상품          |

## Properties parsed
All the properties that the scraper collects and saves to the data storage.

### Common properties
The properties that are common for each product category:

- Title - the assigned name to the product
- Model - the concrete model of the product
- Item category - the product type
- Standard price - the original price of the product
- Member price - the price of the product under the condition of ordering the product from the samsung.com
- Benefit price - the price with the temporary discount under the same condition as for the member price. Applied torwards the standard price
- Benefit price validity period - the period of validity of the discount
- Coupon discount quantity - the coupon discount in the currency. 
- Coupon discount validity period - the period of validity of the coupon 
- Price with coupon discount - the price with the coupon discount under the same condition as for the member price. Applied torwards standard price or the benefit price if the latter is presented
- Outlet special price - the outlet price under the same condition as for member price. Applied torwards the standard price
- Color - the color of the product
- Rating - the 0 to 5 rating of the product
- Quantity of reviews - the amount of feedbacks from the purchases
- Additional properties - the additional properties of the product depending on the product category

### Additional properties based on item category
The properties that might diverse depending on the product category:

- Storage capacity - the data storage capacity of the product
- Screen size - the screen resolution of the product
- Size - the product's diagonal size
- Option - the mount type of the product
