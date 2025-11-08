import requests
from tkinter import *
from tkinter import ttk
import tkcalendar

# ---------------------------
# Global Variables
# ---------------------------
total_usd = 0.0  # Track total converted expenses in USD


# ---------------------------
# Helper Functions
# ---------------------------

def convert_to_usd(amount: float, currency: str) -> float:
    """
    Convert the given amount from specified currency to USD using Fixer API.
    Returns the converted value in USD or raises an Exception on failure.
    """
    url = "https://api.apilayer.com/fixer/convert"
    headers = {"apikey": "YOUR_API_KEY_HERE"}
    params = {"to": "USD", "from": currency, "amount": amount}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise exception for bad response

    data = response.json()
    return float(data.get("result", 0.0))


def add_expense():
    """
    Get input from user, convert to USD, insert into table,
    and update total USD label.
    """
    global total_usd

    try:
        # --- Get user input values ---
        amount = float(entry_amount.get())
        currency = combo_currency.get()
        category = combo_category.get()
        payment = combo_payment.get()
        date = date_entry.get_date()

        if amount <= 0:
            total_label.config(text="⚠️ Please enter an amount greater than 0.")
            return

        # --- Convert to USD using API ---
        converted_usd = convert_to_usd(amount, currency)

        # --- Update total ---
        total_usd += converted_usd

        # --- Insert new expense into table ---
        new_row = (amount, currency, category, payment, date)
        expense_table.insert("", "end", values=new_row, tags=("highlight",))

        # --- Update total label ---
        total_label.config(text=f"💵 Total in USD: {total_usd:.2f}")

    except ValueError:
        total_label.config(text="⚠️ Error: Please enter a valid number for amount.")
    except requests.RequestException:
        total_label.config(text="❌ API Error: Unable to fetch conversion.")
    except Exception as e:
        total_label.config(text=f"⚠️ Unexpected Error: {e}")


# ---------------------------
# UI Setup
# ---------------------------
app = Tk()
app.title("💰 Expense Tracker")
app.geometry("1000x700")
app.config(bg="#B3D8A8")

# --- Title ---
Label(app, text="Expense Tracker", font=("Arial", 20, "bold"),
      bg="#B3D8A8", fg="#E95793").pack(pady=20)

# --- Input Frame ---
frame_inputs = Frame(app, bg="#B3D8A8")
frame_inputs.pack(side=TOP, pady=10)

# --- Amount ---
Label(frame_inputs, text="Amount", font=("Arial", 12, "bold"),
      bg="#B3D8A8", fg="#687FE5").grid(row=0, column=0, pady=5, sticky=W)
entry_amount = Entry(frame_inputs, font=("Arial", 11))
entry_amount.grid(row=0, column=1, padx=(20, 40))

# --- Currency ---
Label(frame_inputs, text="Currency", font=("Arial", 12, "bold"),
      bg="#B3D8A8", fg="#687FE5").grid(row=1, column=0, pady=5, sticky=W)
combo_currency = ttk.Combobox(frame_inputs, values=["USD", "EUR", "EGP"],
                              state="readonly", font=("Arial", 10))
combo_currency.set("EGP")
combo_currency.grid(row=1, column=1, padx=(20, 40))

# --- Category ---
Label(frame_inputs, text="Category", font=("Arial", 12, "bold"),
      bg="#B3D8A8", fg="#687FE5").grid(row=2, column=0, pady=5, sticky=W)
combo_category = ttk.Combobox(frame_inputs,
                              values=["Life Expenses", "Electricity", "Gas",
                                      "Rental", "Grocery", "Savings",
                                      "Education", "Charity"],
                              state="readonly", font=("Arial", 10))
combo_category.set("Life Expenses")
combo_category.grid(row=2, column=1, padx=(20, 40))

# --- Payment Method ---
Label(frame_inputs, text="Payment Method", font=("Arial", 12, "bold"),
      bg="#B3D8A8", fg="#687FE5").grid(row=3, column=0, pady=5, sticky=W)
combo_payment = ttk.Combobox(frame_inputs,
                             values=["Cash", "Credit Card", "Paypal"],
                             state="readonly", font=("Arial", 10))
combo_payment.set("Cash")
combo_payment.grid(row=3, column=1, padx=(20, 40))

# --- Date ---
Label(frame_inputs, text="Date", font=("Arial", 12, "bold"),
      bg="#B3D8A8", fg="#687FE5").grid(row=4, column=0, pady=5, sticky=W)
date_entry = tkcalendar.DateEntry(frame_inputs)
date_entry.grid(row=4, column=1, padx=(20, 40))

# --- Add Button ---
Button(frame_inputs, text="Add Expense", font=("Arial", 10, "bold"),
       bg="#4E71FF", fg="#FFFFFF", command=add_expense,
       padx=10, pady=3).grid(row=5, column=1, pady=15)

# ---------------------------
# Expense Table Section
# ---------------------------
frame_table = Frame(app, bg="#A0C878")
frame_table.pack(side=TOP, pady=25)

columns = ["Amount", "Currency", "Category", "Payment Method", "Date"]
expense_table = ttk.Treeview(frame_table, columns=columns, show="headings", height=10)

# Define columns and headings
for col in columns:
    expense_table.heading(col, text=col, anchor=CENTER)
    expense_table.column(col, anchor=CENTER, width=150)

expense_table.grid(row=0, column=0, sticky="nsew")

# Highlight style for new rows
expense_table.tag_configure("highlight", background="#A4CCD9",
                            font=("TkDefaultFont", 10, "bold"))

# Style headers
style = ttk.Style()
style.configure("Treeview.Heading", font=("TkDefaultFont", 10, "bold"),
                foreground="#4B70F5")

# ---------------------------
# Total USD Label
# ---------------------------
total_label = Label(app, text="💵 Total in USD: 0.00",
                    font=("Arial", 14, "bold"),
                    fg="#E95793", bg="#F0F0F0")
total_label.pack(pady=10)

# ---------------------------
# Start App
# ---------------------------
app.mainloop()
