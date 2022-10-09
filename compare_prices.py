import requests
import json

import sys

sys.path.insert(0, 'bs4.zip')
from bs4 import BeautifulSoup

# Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs, product_glomark):
    # TODO: Aquire the web pages which contain product Price

    html1 = requests.get(product_laughs, headers=user_agent).content
    soup1 = BeautifulSoup(html1, 'html.parser')

    html2 = requests.get(product_glomark, headers=user_agent).content
    soup2 = BeautifulSoup(html2, 'html.parser')
    # TODO: LaughsSuper supermarket website provides the price in a span text.

    price_box1 = soup1.find("div", class_="price-box")
    pricelaugf = price_box1.text.strip()
    price_laughs = float(pricelaugf.split('.')[1])

    product_name_laughs = soup1.find(["h1", ]).text

    # TODO: Glomark supermarket website provides the data in jason format in an inline script.
    # You can use the json module to extract only the price

    s = soup2.select_one('script[type="application/ld+json"]')
    data = json.loads(s.text)
    price_glomark = float(data["offers"][0]["price"])

    product_name_glomark = soup2.find(["h1", ]).text

    # TODO: Parse the values as floats, and print them.

    print('Laughs  ', product_name_laughs, 'Rs.: ', price_laughs)
    print('Glomark ', product_name_glomark, 'Rs.: ', price_glomark)

    if (price_laughs > price_glomark):
        print('Glomark is cheaper Rs.:', price_laughs - price_glomark)
    elif (price_laughs < price_glomark):
        print('Laughs is cheaper Rs.:', price_glomark - price_laughs)
    else:
        print('Price is the same')
