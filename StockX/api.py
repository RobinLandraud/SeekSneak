from bs4 import BeautifulSoup
import requests
import json
from random import randint
from Sizing.SizeChart import MenChartUStoEU, WomenChartUStoEU

class APIProductSX:
    def __init__(self, item = None, sizes = None, brand = "nike") -> None:
        if item is None or sizes is None or brand is None:
            return
        self.parseDataItem(item, sizes, brand)
    def parseDataItem(self, item, sizes, brand):
        self.brand = brand
        self.styleID = item['styleId']
        self.name = item['title']
        self.gender = item['gender']
        self.colorway = item['colorway']
        self.url = 'https://stockx.com/en-gb/' + item['urlKey']
        self.image = item['media']['smallImageUrl']
        self.salesLast72Hours = item['market']['salesLast72Hours']
        self.year = item['year']
        self.sizes = sizes
    def printInfos(self):
        print(f"StyleID: {self.styleID}\n\
        Name: {self.name}\n\
        Colorway: {self.colorway}\n\
        URL: {self.url}\n\
        Image: {self.image}\
        ")
        for size in self.sizes:
            size.printInfos()

class Size:
    def __init__(self, item = None, gender = "men", brand = "nike") -> None:
        if item is None:
            return
        self.parseDataItem(item, gender, brand)
    def parseDataItem(self, item, gender, brand):
        if gender == "men":
            print("is men")
            self.size = f"{MenChartUStoEU(item['shoeSize'], brand)} EU / {item['shoeSize']} US"
        else:
            print("is women")
            self.size = f"{WomenChartUStoEU(str(item['shoeSize']).replace('W', ''), brand)} EU / {item['shoeSize']} US"
        self.lastSale = item['market']['lastSale']
        self.lowestAsk = item['market']['lowestAsk']
        self.volatility = item['market']['volatility']
        self.highestBid = item['market']['highestBid']
    def printInfos(self):
        print(f"Size: {self.size}\n\
        Last Sale: {self.lastSale}\n\
        Lowest Ask: {self.lowestAsk}\n\
        Volatility: {self.volatility}\n\
        Highest Bid: {self.highestBid}\
        ")

def APIsearchSX(query, proxies):
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
    url = f'https://stockx.com/api/browse?_search={query}'
    if proxies is not None:
        html = requests.get(url=url, headers=headers, proxies=proxies[randint(0, len(proxies) - 1)])
    else:
        html = requests.get(url=url, headers=headers)
    output = json.loads(html.text)
    if "captcha" in str(output):
        print("captcha !")
        return None

    url2 = f"https://stockx.com/api/products/{output['Products'][0]['urlKey']}?includes=market&currency=EUR&country=FR"
    if proxies is not None:
        html2 = requests.get(url=url2, headers=headers, proxies=proxies[randint(0, len(proxies) - 1)])
    else:
        html2 = requests.get(url=url2, headers=headers)
    output2 = json.loads(html2.text)
    if "captcha" in str(output):
        print("captcha !")
        return None

    sizes = output2['Product']['children']
    sizeList = []
    for size in sizes:
        if str(sizes[size]['shoeSize']).find("2E") == -1 and str(sizes[size]['shoeSize']).find("3E") == -1:
            new_size = Size(sizes[size], str(output['Products'][0]['gender']), str(output2['Product']['brand']))
            sizeList.append(new_size)

    result = APIProductSX(output['Products'][0], sizeList, str(output2['Product']['brand']))
    print("request done")
    return result