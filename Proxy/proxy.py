from bs4 import BeautifulSoup
import requests

def getListProxies():
    Proxies = []
    data = None
    try:
        data = open("proxies.txt", "r")
    except FileNotFoundError:
        print("proxie.txt not found")
        return None
    for line in data:
        error = False
        elements = line[:-1].split(":")
        proxy = {f"{elements[2]}": f"{elements[0]}:{elements[1]}"}
        try:
            test = requests.get("https://www.google.com/", proxies=proxy, timeout=5)
        except:
            error = True
            print(f"error : {proxy}")
        if not error:
            Proxies.append(proxy)
            print(proxy)
    data.close()
    return Proxies