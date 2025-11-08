# 💰 Expense Tracker (Python + Tkinter)

A simple and elegant **Expense Tracker App** built using **Python (Tkinter)** that helps you manage and track your daily expenses.  
It allows you to record your expenses with different currencies, categories, and payment methods — and automatically converts all amounts to **USD** using the **Fixer API**.

## 🧩 Features

- ✅ Add expenses with amount, currency, category, payment method, and date
- 💵 Automatically converts all expenses to **USD** using a real-time exchange rate API
- 📊 Displays all expenses in a table format
- 🔢 Calculates and displays total expenses in USD
- 🧠 Input validation and error handling (invalid numbers, API errors, etc.)
- 🎨 Clean and modern Tkinter UI design

## 🛠️ Technologies Used

- **Python 3.8+**
- **Tkinter** — GUI framework
- **tkcalendar** — for date selection widget
- **requests** — for making API calls
- **Fixer API** — currency conversion service

## 📋 How It Works

1. Enter your amount and select currency, category, payment method, and date.

2. Click the "Add Expense" button.

3. The app will:

   - Convert your amount to USD using the API.

   - Add the expense to the table below.

   - Update the total expenses label in USD.

4. Invalid inputs or API issues will show an error message.

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
  - git clone https://github.com/baselelsrogy/small-projects-python-chatGPT
  - cd "Expense Tracker"
  - python expense_tracker.py
```

### 2️⃣ Install Dependencies

```bash
  - pip install requests tkcalendar tkinter
```

## ⚙️ Configuration

1. The app uses Fixer API for currency conversion.
   You’ll need an API key from Fixer.io

2. Sign up at [Fixer.io](https://fixer.io/signup/free)

3. Get your free API key.

4. Replace the placeholder key inside the code:

   ```python
     - headers = {"apikey": "YOUR_API_KEY_HERE"}
   ```
