from bs4 import BeautifulSoup
import requests
import json
from random import randint
from Sizing.SizeChart import MenChartUEtoUS, WomenChartUEtoUS

def parseRProductPageSizes(url, gender, brand, proxies):
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
    html = requests.get(url=url, headers=headers, proxies=proxies[randint(0, len(proxies) - 1)])
    soup = BeautifulSoup(html.text, "lxml")
    sizes = []
    blocks = soup.find("ul", class_="select__size__list").find_all("li")
    for block in blocks:
        size = (str(block.find("span"))[19:-7]).replace(" ½", ".5").replace(" ⅓", " 1/3").replace(" ⅔", " 2/3")
        price = block.find("span", class_="float-right price")
        res = str(price)[32:-7]
        if res != "Informez-moi":
            res = str(price.find("span"))[15:-7]
        else:
            res = "?"
        stock = str(block.find("span", class_="float-right delivery__text"))[42:-70]
        if stock.replace(" ", "") == "":
            stock = "4+"
        else:
            stock = stock[10:-9]
        if gender == "men":
            sizes.append({
                'shoeSize': f"{size} EU / {MenChartUEtoUS(size, brand)} US",
                'price': res,
                'stock': stock
            })
        else:
            sizes.append({
                'shoeSize': f"{size} EU / {WomenChartUEtoUS(size, brand)} US",
                'price': res,
                'stock': stock
            })
    return sizes
