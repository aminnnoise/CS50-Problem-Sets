import sys
import requests

n = ""
try :
    if len(sys.argv) == 2:
        n = sys.argv[1]
        n = float(n)

except IndexError:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer <Your API Key>'
    }
    respond = requests.get(url, headers=headers)
    respond.raise_for_status()
    data = respond.json()
    btc_price = float(data['data']['priceUsd'])
except requests.RequestException:
    sys.exit()

total_cost = n * btc_price
print(f"${total_cost:,.4f}")