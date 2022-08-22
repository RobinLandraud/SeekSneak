#!/usr/bin/env python3
from website import create_app

app = create_app()

def main():
    #data = search("dunk")
    #dunk = APIProductSX(data)
    #dunk.printInfos()
    #most_popular(2)
    #print("start")
    #parser_most_popular(1, proxies)
    parse()
    #most_popular(2, proxies)


if __name__ == "__main__":
    app.run(debug=False)
    #main()