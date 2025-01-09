# python -m pip install requests
# => get data from web (html, json, xml)
# python -m pip install beautifulsoup4
# => parse html

# git config --global user.name "Ramesh Pradhan"
# git config --global user.email "pyrameshpradhan@gmail.com"


import json
import requests
from bs4 import BeautifulSoup


URL = "http://books.toscrape.com/"


def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error")
        return

    # Set encoding explicitly to handle special characters
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    all_books = []
    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1:]
        formatted_book = {
            "title": title,
            "currency": currency,
            "price": price,
        }
        all_books.append(formatted_book)

    return all_books


books = scrape_books(URL)
with open("books.json", "w") as f:
    json.dump(books, f, indent=2)
