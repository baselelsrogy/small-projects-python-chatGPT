# 💱 Currency Converter (Using Fixer API)

This Python script allows you to **convert currency values** between two different currencies using the [Fixer API](https://apilayer.com/marketplace/fixer-api).  
It prompts the user for input, validates it, and then displays the converted result.

---

## 🧠 How It Works

1. The user is prompted to enter:
   - The **initial currency** (e.g., `USD`)
   - The **target currency** (e.g., `EUR`)
   - The **amount** to convert
2. The script validates that:
   - The amount entered is numeric
   - The amount is greater than zero
3. It sends a GET request to the Fixer API with:
   - The currencies and amount
   - An API key (required)
4. The script prints the converted amount if the request succeeds, or an error message otherwise.

---

## 🧩 Example Usage

```bash
- Enter an initial currency: USD
- Enter a target currency: EUR
- Enter the amount: 100
- Done convert 100.0USD from USD to EUR: 93.45EUR
```

## ⚙️ Requirements

1. Python 3.x
2. requests library
3. You can install the dependency with:
   ```bash
       pip install requests
   ```
