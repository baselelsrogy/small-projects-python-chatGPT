import requests

def get_exchange_rate(from_currency, to_currency):
    """
    Fetch real-time exchange rate between two currencies
    using the ExchangeRate API (https://api.exchangerate-api.com/).
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("⚠️ Error: Could not retrieve exchange rates.")
        return None
    
    data = response.json()
    rates = data.get("rates", {})
    return rates.get(to_currency.upper())


def get_valid_amount():
    """
    Keep asking user for a valid amount (must be numeric and > 0).
    """
    while True:
        try:
            amount = float(input("Enter amount to convert: "))
            if amount <= 0:
                print("❌ Invalid amount! Please enter a value greater than 0.")
            else:
                return amount
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")


def main():
    print("=== Currency Converter ===")
    
    while True:
        # Step 1: Get valid amount
        amount = get_valid_amount()
        
        # Step 2: Get currency codes
        from_currency = input("Convert from (e.g. USD, EUR, GBP): ").strip()
        to_currency = input("Convert to (e.g. USD, EUR, GBP): ").strip()
        
        # Step 3: Get exchange rate
        rate = get_exchange_rate(from_currency, to_currency)
        if rate is None:
            print("⚠️ Could not find exchange rate. Check your currency codes.\n")
            continue  # Ask again
        
        # Step 4: Calculate conversion
        converted_amount = amount * rate
        print(f"\n💱 {amount:.2f} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}\n")
        
        # Step 5: Ask if user wants to convert again
        again = input("Do you want to convert another amount? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("👋 Goodbye!")
            break


if __name__ == "__main__":
    main()
