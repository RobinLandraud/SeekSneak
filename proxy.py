from bs4 import BeautifulSoup
import requests

def getListProxies():
    res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.text,"lxml")
    Proxies = []
    for item in soup.find_all("tr"):
        elems = item.find_all("td", attrs={'class': None, 'title': None})
        if len(elems) == 4 and "." in str(elems[0]) and str(elems[3]) == "<td>elite proxy</td>":
            proxy = {"http": f"http://{str(elems[0])[4:-5]}:{str(elems[1])[4:-5]}"}
            error = False
            try:
                test = requests.get("https://www.google.com/", proxies=proxy, timeout=5)
            except:
                error = True
            if not error:
                Proxies.append(proxy)
                print(Proxies[len(Proxies) - 1])
    return Proxies