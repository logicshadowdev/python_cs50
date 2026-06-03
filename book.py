import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print("Top 5 Books")
    print("=" * 40)

    for index, book in enumerate(books[:5], start=1):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = book.p["class"][1]

        print(f"{index}. {title}")
        print(f"Price: {price}")
        print(f"Rating: {rating}")
        print("-" * 40)

except requests.exceptions.RequestException as e:
    print("Error connection to website")
    print(f"Details: {e}")