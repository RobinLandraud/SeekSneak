from bs4 import BeautifulSoup
import requests
import json
from random import randint

def APIsearchSKU(sku, proxies):
    url = f'https://restocks.net/fr/shop/search?q={sku}&page=1&filters[0][range][price][gte]=1'

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
    output = json.loads(html.text)
    print(output['data'][0]['slug'])
    print("request done")
    if "captcha" in str(output):
        print("captcha !")
        return None
    return output['data'][0]