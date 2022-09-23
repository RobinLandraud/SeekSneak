#!/usr/bin/env python3
from website import create_app

from Goat.api import APIsearchG
from Proxy.proxy import getListProxies

app = create_app()

def main():
    #data = search("dunk")
    #dunk = APIProductSX(data)
    #dunk.printInfos()
    #most_popular(2)
    #parser_most_popular(1, proxies)
    proxies = getListProxies()
    APIsearchG("DD1391-100", proxies)
    #most_popular(2, proxies)


if __name__ == "__main__":
    app.run(debug=False)
    #main()