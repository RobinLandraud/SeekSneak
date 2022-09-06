from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests
import json
from random import randint
from Sizing.SizeChart import MenChartUStoEU, WomenChartUStoEU

class APIProductG:
    def __init__(self, item = None, sizes = None) -> None:
        if item is None or sizes is None:
            return
        self.parseDataItem(item, sizes)
    def parseDataItem(self, item, sizes):
        self.templateID = item['templateID']
        self.gender = item['gender']
        self.name = item['name']
        self.styleID = item['styleId']
        self.url = item['url']
        self.brand = item['brand']
        self.sizes = sizes
    def printInfos(self):
        print(f"templateID: {self.templateID}\n\
        gender: {self.gender}\n\
        name: {self.name}\n\
        styleId: {self.styleID}\n\
        url: {self.url}\n\
        brand: {self.brand}\
        ")
        for size in self.sizes:
            size.printInfos()

class Size:
    def __init__(self, item = None) -> None:
        if item is None:
            return
        self.parseDataItem(item)
    def parseDataItem(self, item):
        self.size = item['shoeSize']
        self.stockStatus = item['stockStatus']
        self.lowestPrice = item['lowestPrice']
        self.instantShipLowestPrice = item['instantShipLowestPrice']
        self.lastSoldPrice = item['lastSoldPrice']
    def printInfos(self):
        print(f"Size: {self.size}\n\
        Stock: {self.stockStatus}\n\
        Stock: {self.lowestPrice}\n\
        Stock: {self.instantShipLowestPrice}\n\
        Price: {self.lastSoldPrice}\
        ")

def GOATcheckAmount(item):
    if "amount" in item:
        return str(item['amount'] / 100)
    return "?"

def GOATgetSizesAPI(productID, brand, proxies):
    sizes = []
    url = f'http://www.goat.com/web-api/v1/product_variants/buy_bar_data?productTemplateId={productID}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:20.0) Gecko/20121202 Firefox/20.0',
        'Content-Type': 'application/json',
        'accept-language': 'fr-FR'
    }
    proxy = proxies[randint(0, len(proxies) - 1)]
    with requests.Session() as s:
        s.get(url=url, headers=headers, proxies=proxy)
        s.cookies.set('currency', 'EUR')
        s.cookies.set('country', 'FR')
        html = s.get(url=url, headers=headers, proxies=proxy)
    output = json.loads(html.text)
    for size in output:
        if size['shoeCondition'] != "used":
            item = {
                "shoeSize": str(size['sizeOption']['value']),
                "stockStatus": size['stockStatus'],
                "lowestPrice": GOATcheckAmount(size['lowestPriceCents']),
                "instantShipLowestPrice": GOATcheckAmount(size['instantShipLowestPriceCents']),
                "lastSoldPrice": GOATcheckAmount(size['lastSoldPriceCents'])
            }
            sizes.append(Size(item))
    return sizes

def APIsearchSKU(sku, proxies):

    url = 'https://2fwotdvm2o-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.25.1%3Breact%20(16.9.0)%3Breact-instantsearch%20(6.2.0)%3BJS%20Helper%20(3.1.0)&x-algolia-application-id=2FWOTDVM2O&x-algolia-api-key=ac96de6fef0e02bb95d433d8d5c7038a'

    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/fr-fr',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    body = '{"requests":[{"indexName":"product_variants_v2","params":"distinct=true&maxValuesPerFacet=1&page=0&query=' + sku + '&facets=%5B%22instant_ship_lowest_price_cents"}]}'
    #html = requests.get(url=url, headers=headers, proxies=proxies[randint(0, len(proxies) - 1)])
    html = requests.post(url=url, data=body, headers=headers, proxies=proxies[randint(0, len(proxies) - 1)])
    output = json.loads(html.text)
    productID = output['results'][0]['hits'][0]['product_template_id']
    productURL = f"https://www.goat.com/sneakers/{str(output['results'][0]['hits'][0]['slug'])}"
    productSKU = output['results'][0]['hits'][0]['sku']
    productBrand = output['results'][0]['hits'][0]['size_brand']
    productGender = output['results'][0]['hits'][0]['gender']
    productName = output['results'][0]['hits'][0]['name']

    item = {
        "templateID": str(productID),
        "url": str(productURL),
        "styleId": str(productSKU),
        "brand": str(productBrand),
        "gender": str(productGender),
        "name": str(productName)
    }
    return item

def APIsearchG(sku, proxies):
    item = APIsearchSKU(sku, proxies)
    sizes = GOATgetSizesAPI(item['templateID'], item['brand'], proxies)
    result = APIProductG(item, sizes)
    result.printInfos()
    return result