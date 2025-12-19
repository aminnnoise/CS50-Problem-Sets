import requests
import sys

if len(sys.argv) == 2:
    
    try:
        user_input = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    url = "https://rest.coincap.io/v3/price/bysymbol/BTC"
    header = {
        'accept': 'application/json',
        'Authorization': 'Bearer 07c7bfdfb0b6d1eaac834ce4b3dc47e5df8c930b5f355c3a9d179996fdf8a7ed'
    }
    answer = requests.get(url , headers=header).json()
    price = float(answer['data'][0])
    price = price * user_input
    print(f"${price:,.4f}")
    sys.exit(0)

except (requests.RequestException, ValueError):
    print("Error")
    sys.exit(1)
