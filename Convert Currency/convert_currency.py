import requests

init_currency = input("Enter an initial currency: ").upper()
target_currency = input("Enter an target currency: ").upper()

while True:
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("The amount must be a numeric value!")
        continue
    
    if amount == 0:
        print("The amount must be greater than 0")
        continue
    else:
        break


url = "https://api.apilayer.com/fixer/convert"
params = {
    "to": target_currency,
    "from": init_currency,
    "amount": amount
}

headers = {
    "apikey": "YOUR-API-KEY-HERE"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    result = response.json()
    amount_converter = result['result']
    print(f"Done convert {amount}{init_currency} from {init_currency} to {target_currency}: {amount_converter}{target_currency}")
else:
    print(f"Error: {response.status_code}, {response.text}")
