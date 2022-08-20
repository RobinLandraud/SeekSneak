from bs4 import BeautifulSoup
import requests
import json
from random import randint

class ProductSX:
    def __init__(self, item = None) -> None:
        if item is None:
            return
        self.parseDataItem(item)
    def parseDataItem(self, item):
        self.styleID = item['styleId']
        self.lastSale = item['market']['lastSale']
        self.colorway = item['colorway']
        self.url = 'https://stockx.com/en-gb/' + item['urlKey']
        self.lowestAsk = item['market']['lowestAsk']
        self.image = item['media']['smallImageUrl']
        self.uuid = item['market']['productUuid']
        self.nbrAsks = item['market']['numberOfAsks']
        self.nbrbids = item['market']['numberOfBids']
        self.volatility = item['market']['volatility']
        self.salesLast72Hours = item['market']['salesLast72Hours']
        self.lastSaleDate = item['market']['lastSaleDate']
    def printInfos(self):
        print(f"StyleID: {self.styleID}\n\
        Last Sale: {self.lastSale}\n\
        Colorway: {self.colorway}\n\
        URL: {self.url}\n\
        Lowest Ask: {self.lowestAsk}\n\
        Image: {self.image}\n\
        UUID: {self.uuid}\n\
        Number of Asks: {self.nbrAsks}\n\
        Number of Bids: {self.nbrbids}\n\
        Volatility: {self.volatility}\n\
        Sales in last 72 Hours: {self.salesLast72Hours}\n\
        Last Sale Date: {self.lastSaleDate}\n\
        ")

def search(query, proxies):
    url = f'https://stockx.com/api/browse?_search={query}'

    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/en-gb',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    html = requests.get(url=url, headers=headers, proxies=proxies[randint(0, len(proxies) - 1)])
    output = json.loads(html.text)
    if "captcha" in str(output):
        return None
    return output['Products'][0]