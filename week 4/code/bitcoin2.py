import sys
import requests

n = ""
try :
    if len(sys.argv) == 2:
        n = sys.argv[1]
        n = float(n)

except IndexError:
    sys.exit()
except ValueError:
    sys.exit()

try:
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer 07c7bfdfb0b6d1eaac834ce4b3dc47e5df8c930b5f355c3a9d179996fdf8a7ed'
    }
    respond = requests.get(url, headers=headers)
    respond.raise_for_status()
    data = respond.json()
    btc_price = float(data['data']['priceUsd'])
except requests.RequestException:
    sys.exit()

total_cost = n * btc_price
print(f"${total_cost:,.4f}")