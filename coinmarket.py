import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status

    soup = BeautifulSoup(response.text, "html.parser")

    print("LIVE CRYPTO PRICES")
    print("=" * 40)

    coins = soup.find_all("tr")[1:10]

    for coin in coins:
        cols = coin.find_all("td")

        if len(cols) > 3:
            name = cols[2].text.strip()
            price = cols[3].text.strip()

            print(f"Coin: {name}")
            print(f"Price: {price}")
            print("=" * 40)

except requests.exceptions.RequestException:
    print("Failed to fetch crypto prices")