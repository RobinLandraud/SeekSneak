from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from api import search, ProductSX

def parser_most_popular_page(index):
    result = []
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(f"https://stockx.com/fr-fr/sneakers/most-popular?page={index}")
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "lxml")
    driver.close()
    elements = soup.find_all("p", class_="chakra-text css-3lpefb")
    for elem in elements:
        result.append(str(elem)[34:-4])
    return result

def parser_most_popular(nbr, proxies):
    result = []
    for i in range(1, nbr + 1):
        elements = parser_most_popular_page(i)
        for elem in elements:
            shoes = search(elem, proxies)
            if shoes is not None:
                prod = ProductSX(shoes)
                prod.printInfos()
                result.append(prod)
    return result

