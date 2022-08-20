#!/usr/bin/env python3
from api import ProductSX, search
from proxy import getListProxies
from parser import parser_most_popular

from website import create_app

app = create_app()

def main():
    #data = search("dunk")
    #dunk = ProductSX(data)
    #dunk.printInfos()
    #most_popular(2)
    print("start")
    proxies = getListProxies()
    parser_most_popular(1, proxies)

    #most_popular(2, proxies)


if __name__ == "__main__":
    app.run(debug=True)
    #main()