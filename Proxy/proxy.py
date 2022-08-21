from bs4 import BeautifulSoup
import requests

def getListProxies():
    res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.text,"lxml")
    Proxies = []
    for item in soup.find_all("tr"):
        elems = item.find_all("td", attrs={'title': None})
        if len(elems) == 8 and "." in str(elems[0]) and str(elems[4]) == "<td>elite proxy</td>" and str(elems[5]) == '<td class="hm">yes</td>' and str(elems[6]) == '<td class="hx">yes</td>':
            proxy = {"http": f"http://{str(elems[0])[4:-5]}:{str(elems[1])[4:-5]}"}
            error = False
            try:
                test = requests.get("https://www.google.com/", proxies=proxy, timeout=5)
            except:
                error = True
                print(f"error : {proxy}")
            if not error:
                Proxies.append(proxy)
                print(Proxies[len(Proxies) - 1])
    return Proxies