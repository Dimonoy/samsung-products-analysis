# Samsung.com scraper
The scraper utilizes the API endpoint, which is used by the samsung.com during the product
catalog webpages loading.  
The key characteristics of the API:
- the Fetch/XHR request is performed by the client product catalog page;
- the request parameter for specification of the product category is called a
"product classification number" ([See the table below](#product-categories));
- the response contains all the possible information for each product presented in the catalog;
- the request is easily adjustable to receive the desired amount of items and category.

## Product categories
There are in total 38 product categories presented on the https://www.samsung.com/sec/ (Korean).
Product category names are taken from the product catalog URLs to those product categories.
Each product classification number was manually collected from each page using "DevTools".

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
All the properties that the scraper collects and saves to the data storage are presented in this
chapter.

The properties that are common for each product category:

- _Title_ (`goodsNm`) - the assigned name to the product
- _Model_ (`mdlNm`) - the model name of the product
- _Model code_ (`mdlCode`) - the model's code name
- _Link_ (`goodsDetailUrl`) - the URL to the product
- _Item category_ (`compDispClsfEnNm`) - the product type
- _Item classification number_ (`compDispClsfNo`) - the assigned by Samsung number for the
product type
- _Standard price_ (`priceStr[2]`) - the original price of the product
- _Member price_ (`priceStr[3]`) - the price of the product under the condition of ordering
the product from the samsung.com
- _Benefit price_ (`priceStr[4]`) - the price with the temporary discount under the same
condition as for the member price. Applied torwards the standard price
- _Coupon discount_ (`cpAllDcAmt`) - the coupon discount in the currency. 
- _Outlet special price_ (`priceStr[5]`) - the outlet price under the same condition as
for member price. Applied torwards the standard price
- _Rating_ (`reviewGrade`) - the 0 to 5 rating of the product
- _Quantity of reviews_ (`reviewCount`) - the amount of feedbacks from the purchases
- _Stock quantity_ (`stockQty`) - the quantity of the product available
- _Additional properties_ (`goodsOptStr`) - the additional properties of the product depending on
the product category. JSON of additional properties is scraped from this option.
- _Date time_ (`datetime.now()`) - the date and time the product's records were scraped

## API description

### Products price complication
The product's prices are calculated from the API properties and then displayed on the webpage,
which requires an elaboration on what to take. Full product's JSON response can be found [here](#sample-response)
There are in total 8 types of price combinations:
1. _No price_ (sale price equals 0). Condition: `if 'activatePhoneYn' exists or priceStr[2] == 0`
2. _Standard price_. Condition: `if priceStr[1] == '00' and priceStr[2] == priceStr[3]`
3. _Standard price_. Condition: `if priceStr[1] != '00' and priceStr[2] == priceStr[3] and priceStr[3] == priceStr[4]`
4. _Standard price_ + _Member price_. Condition: `if priceStr[1] == '00' and priceStr[2] != priceStr[3]`
5. _Standard price_ + _Benefit price_. Condition: `if priceStr[1] != '00' and priceStr[2] == priceStr[3] and priceStr[3] != priceStr[4]`
6. _Standard price_ + _Member price_ + _Benefit price_. Condition: `if priceStr[1] != '00' and priceStr[2] != priceStr[3] and priceStr[3] != priceStr[4]`
7. _Standard price_ + _Outlet specials_. Condition: `if outletFlgYn == "Y"`

> Notes
>
> The variable `priceStr[2]` - Standard price, `priceStr[3]` - Member price, `priceStr[4]` - Benefit price or Outlet special
> The variable `priceStr[0] == '00'` means that the length of the `priceStr` is 4. Otherwise, the `priceStr` length is 5.
> In the `priceStr` of the length 4: `priceStr[2]` - Standard price, `priceStr[3]` - Member price. No benefit price
> There are phones carriers, that do not have price. They have special properties: `activatePhoneYn` and `activatePhonePriceVO` 
> Some products may have a price of 0. That means they are out of stock.

Following API properties can be used to collect all the price combinations:
- `priceStr` - text with prices separated by symbol `|`
- `salePrice` - final price
- `cpAllDcAmt` - coupon discount amount
- `outletFlgYn` - whether the outlet special price presented
- `activatePhoneYn` - the phone carrier is present
- `activatePhonePriceVO` - the phone carrier additional information

## Appendix

### Sample response
```json
{
    "sysRegrNo": null,
    "sysRegrNm": null,
    "sysRegDtm": null,
    "sysUpdrNo": null,
    "sysUpdrNm": null,
    "sysUpdDtm": null,
    "goodsId": "G000261907",
    "goodsNm": "BESPOKE 무풍에어컨 클래식 (56.9 ㎡ + 18.7 ㎡)",
    "mdlCode": "AF17B7939WZSRT",
    "mdlNm": "AF17B7939WZSRT",
    "compNo": 312,
    "priceStr": "619224|10|3140000|3140000|2049000",
    "curPrice": null,
    "fvtPrice": null,
    "salePrice": 2049000,
    "maxSalePrice": null,
    "minSalePrice": null,
    "imgPath1": "//images.samsung.com/kdp/goods/2022/04/27/10e6174c-bead-434b-88d9-1b5ad8a1ed9e.png",
    "imgPath2": "//images.samsung.com/kdp/goods/2022/03/25/b570e52e-b90d-48c2-a087-30bd29f792d2.gif",
    "imgPath3": "//images.samsung.com/kdp/goods/2022/03/25/4bdc798a-f068-4d45-a3e4-65dd75ed6bf1.png",
    "imgPath4": "//images.samsung.com/kdp/goods/2022/03/25/b94a410f-938e-46f0-ada4-5a924cc2c03d.png",
    "grpPath": "AF17B7939WZSRT",
    "goodsOptStr": "1|1001|5713|5713|색상|이브닝 코랄|#c88266|Y|AF17B7939WZSRZ|G000261908,G000261836,G000261907,G000261837|color|CottaEveningCoral|\n2|4185|7529|7529|구분|홈멀티||N|AF17B7939WZSRT|G000261907,G000261908|Air conditioner-type|Stand and wall-mounted air conditioner|\n2|4185|7530|7530|구분|스탠드||N|AF17B7939WZST|G000261836,G000261837|Air conditioner-type|stand air conditioner|\n3|2001|2005|2005|배관|일반 배관||N|AF17B7939WZST|G000261836,G000261907|option|일반 배관|\n3|2001|2006|2006|배관|선매립 배관||N|AF17B7939WZSZ|G000261837,G000261908|option|선매립 배관|",
    "wishYn": null,
    "ctgRank": 55,
    "reviewGrade": 4.9,
    "reviewCount": 137,
    "familyReviewGrade": 5,
    "bomReviewGrade": 672,
    "familyReviewCount": 1,
    "bomReviewCount": 136,
    "stockQty": 86,
    "flagStr": "설치상품",
    "saleStatCd": "12",
    "goodsPath": null,
    "membershipPoint": 2049,
    "membershipYn": "N",
    "goodsDetailUrl": "air-conditioners/AF17B7939WZSRT/AF17B7939WZSRT/",
    "bnrText": null,
    "bnrImgPath": null,
    "bnrMobileImgPath": null,
    "bnrMobileImgPath2": null,
    "dispCornTpCd": null,
    "cardTpCd": null,
    "showPstCd": null,
    "linkUrl": null,
    "bnrSubText": null,
    "bnrHtml": null,
    "bnrDscrt": null,
    "bnrDscrt2": null,
    "bnrTag": null,
    "bspkGoodsYn": "N",
    "goodsAddTpCd": null,
    "goodsAddTpSubCd": null,
    "uspDesc": "평생보증(디지털 인버터 모터 & 컴프레서 무상수리)\n냉방면적 : 스탠드[62.6 ㎡] + 벽걸이[18.7 ㎡]\n색상 : 스탠드(화이트, 바람문 패널레디) + 벽걸이(플랫 화이트)",
    "uspDescList": [
        "평생보증(디지털 인버터 모터 & 컴프레서 무상수리)",
        "냉방면적 : 스탠드[62.6 ㎡] + 벽걸이[18.7 ㎡]",
        "색상 : 스탠드(화이트, 바람문 패널레디) + 벽걸이(플랫 화이트)"
    ],
    "itdcMsg1": null,
    "goodsPrcNo": 619224,
    "goodsPriceRangeInfoList": null,
    "dispClsfCornNm": null,
    "goodsOrdTpCd": "",
    "tradeInType": null,
    "tradeInTypeCd": null,
    "galaxyClubYn": "N",
    "subDispClsfNo": null,
    "goodsTpCd": "20",
    "useStkCd": "10",
    "imgPresetYn1": "Y",
    "imgPresetYn2": "N",
    "imgPresetYn3": "N",
    "imgPresetYn4": "N",
    "onlineStoreOnlyYn": "N",
    "isHomefitnessGoodsYn": "N",
    "membershipUseExcptYn": "N",
    "compareExcptYn": "N",
    "thirdPartyYn": "N",
    "customGoodsYn": "N",
    "popupCtaDispYn": null,
    "popupCtaNm": null,
    "goodsFlagName": null,
    "colVal1": null,
    "colVal2": null,
    "colVal3": null,
    "colVal4": null,
    "discountRate": null,
    "minDiscountRange": null,
    "maxDiscountRange": null,
    "discountRateYn": null,
    "outletFlgYn": "Y",
    "winePickupGoodsYn": null,
    "carePlusType": null,
    "carePlusCode": null,
    "qookerRentalYn": null,
    "stId": 1,
    "bespokeMinimumPrice": null,
    "panelColor": null,
    "bspkPrc1": null,
    "bspkPrc2": null,
    "bspkPrc3": null,
    "bspkPrc4": 0.0,
    "bspkPrc5": 0.0,
    "optionCnt": 0,
    "panelCnt": 0,
    "goodsRcmndCommentList": null,
    "compDispClsfNo": 37010000,
    "compDispClsfNm": null,
    "compDispClsfEnNm": "air-conditioners",
    "priceStr0": null,
    "priceStr1": null,
    "priceStr2": null,
    "priceStr3": null,
    "priceStr4": null,
    "priceStr5": null,
    "priceStr6": null,
    "priceStrLast": null,
    "goodsSleCode": "0",
    "goodsUppackInfo": "N",
    "cpUseYn": "N",
    "goodsDetailVo": null,
    "showCpAmtYn": "Y",
    "showAppCpAmtYn": "Y",
    "homeClsGoodsYn": null,
    "goodsMdlExcptStr": null,
    "goodsMdlExcpt": {
        "": "N",
        "wishExcptYn": "N",
        "omsStockExcptYn": "N",
        "hideBtnOptChg": "N",
        "deliveryDelaySndYn": "N",
        "cartExcptYn": "N",
        "trialYn": "N",
        "netfunnelYn": "N",
        "pdContsExcptYn": "N"
    },
    "clsItemCd": null,
    "homeClsUsePrdCd": null,
    "homeClsSvcGbCd": null,
    "clsCtgryCd": null,
    "timeDlvrAplYn": "N",
    "timeDlvrAplCtgYn": "N",
    "timeDlvrAvlStkYn": "Y",
    "dlvrPckYn": "N",
    "omsSendYn": "Y",
    "midDcRate": 0,
    "webCpAllDcAmt": 0,
    "cpAllDcAmt": 0,
    "totCompVal": null,
    "activatePhoneYn": null,
    "activatePhonePriceVO": null,
    "unpsort": "1",
    "sktSort": "0"
}
```
