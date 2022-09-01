import time
from bs4 import BeautifulSoup
from .api import APIsearchSX, APIProductSX
from datetime import date

from scrapingant_client import ScrapingAntClient

KEY = "6cec014bedb249deb77e42e43378c842"

class ProductSX:
    def __init__(self, item = None) -> None:
        if item is None:
            return
        self.parseDataItem(item)
    def parseDataItem(self, item):
        self.name = item['name']
        self.lowestAsk = item['lowestAsk']
        self.sales = item['sales']
        self.image = item['image']
    def printInfos(self):
        print(f"StyleID: {self.styleID}\n\
        Name: {self.name}\n\
        Lowest Ask: {self.lowestAsk}\n\
        Image: {self.image}\n\
        Sales: {self.sales}\
        ")

def APIscrapPage(page, key):
    print(f"scraping page : {page}")
    client = ScrapingAntClient(token=key)
    result = client.general_request(page)
    print("scraped")
    return (result.content)

def parser_most_popular_page(index):
    result = []
    page = f"https://stockx.com/fr-fr/sneakers/most-popular?page={index}"

    content = APIscrapPage(page, KEY)
    #content = open("page.txt", "r")

    soup = BeautifulSoup(content, "lxml")
    cases = soup.find_all("div", class_="css-h8htgv")

    for case in cases:
        name = case.find("p", class_="chakra-text css-3lpefb")
        image = case.find("img")
        lowestAsk = case.find("p", class_="chakra-text css-9ryi0c")
        solds = case.find("span", class_="css-1h8gyx6")
        item = {
            "name": str(name)[34:-4],
            "image": (str(image).split('src="')[1])[:-3],
            "sales": str(solds)[26:-7],
            "lowestAsk": str(lowestAsk)[34:-4]
        }
        #result.append(str(name)[34:-4])
        result.append(ProductSX(item))
    return result


def parser_most_popular(nbr, proxies):
    result = []
    for i in range(1, nbr + 1):
        elements = parser_most_popular_page(i)
        for elem in elements:
            print(f"elem is {elem.name}")
        result += elements
    return result

