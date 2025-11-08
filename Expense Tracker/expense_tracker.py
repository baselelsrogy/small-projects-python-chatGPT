from tkinter import *
from tkinter import ttk
import tkcalendar
import requests

money_usd = 0.0  # global USD

def add_expense():
  """Get data from user, convert to USD, insert row, and update total"""
  global money_usd

  try:
    # get data
    real_amm = float(get_amount.get())
    curr = get_currency.get()
    cat = get_category.get()
    pay = get_payment.get()
    date = get_entry_date.get_date()
    
    # check the amount not equal "0"
    if real_amm == 0:
      return

    # Convert to USD using API
    url = "https://api.apilayer.com/fixer/convert"
    params = {
        "to": "USD",
        "from": curr,
        "amount": real_amm
    }
    headers = {
      "apikey": "YOUR_API_KEY_HERE"
    }

    response = requests.get(url, headers=headers, params=params)
    
    # to check the response is OK
    if response.status_code == 200:
      result = response.json()
      converted_usd = float(result["result"])

      # update total USD
      money_usd += converted_usd

      # Insert converted row into table
      values = [real_amm, curr, cat, pay, date]
      table.insert("", "end", values=values, tags=("highlight",))

      # Update total label
      total_usd_label.config(text=f"💵 Total in USD: {money_usd:.2f}")
    else:
      total_usd_label.config(text="❌ API Error, try again later")

  except Exception as e:
    total_usd_label.config(text=f"⚠️ Error: Enter an valid amount !")

# Start GUI App
app = Tk()
app.title("Expense Tracker")
app.geometry("1000x700")
app.config(bg="#B3D8A8")

# title
title_app = Label(app, text="Expense Tracker", font="Arial 20 bold", bg="#B3D8A8", fg="#E95793")
title_app.pack(pady=20)

# Frame up
frame_up = Frame(app, bg="#B3D8A8")
frame_up.pack(side=TOP)

# Amount
amount = Label(frame_up, text="Amount", font="Arial 12 bold", bg="#B3D8A8", fg="#687FE5")
amount.grid(row=0, column=0)
get_amount = Entry(frame_up, font="Arial 11")
get_amount.grid(row=0, column=1, padx=(100, 0))

# Currency
currency = Label(frame_up, text="Currency", font="Arial 12 bold", bg="#B3D8A8", fg="#687FE5")
currency.grid(row=1, column=0, pady=10)
get_currency = ttk.Combobox(frame_up, values=["EUR", "EGP", "USD"], state="readonly", font="Arial 10")
get_currency.set("EGP")
get_currency.grid(row=1, column=1, padx=(100, 0))

# Category
category = Label(frame_up, text="Category", font="Arial 12 bold", bg="#B3D8A8", fg="#687FE5")
category.grid(row=2, column=0, pady=10)
get_category = ttk.Combobox(frame_up, values=["Life Expenses", "Electricity", "Gas", "Rental", "Grocery", "Savings", "Education", "Charity"], state="readonly", font="Arial 10")
get_category.set("Life Expenses")
get_category.grid(row=2, column=1, padx=(100, 0))

# Payment method
payment = Label(frame_up, text="Payment Method", font="Arial 12 bold", bg="#B3D8A8", fg="#687FE5")
payment.grid(row=3, column=0, pady=10)
get_payment = ttk.Combobox(frame_up, values=["Cash", "Credit Card", "Paypal"], state="readonly", font="Arial 10")
get_payment.set("Cash")
get_payment.grid(row=3, column=1, padx=(100, 0))

# Date
entery_date = Label(frame_up, text="Date", font="Arial 12 bold", bg="#B3D8A8", fg="#687FE5")
entery_date.grid(row=4, column=0, pady=10)
get_entry_date = tkcalendar.DateEntry(frame_up)
get_entry_date.grid(row=4, column=1, padx=(100, 0))

# Button Add Expense
add_btn = Button(frame_up, text="Add Expense", font="Arial 10 bold", bg="#4E71FF", fg="#F2F2F2", command=add_expense)
add_btn.grid(row=5, column=2, pady=5)

# Frame Down
frame_down = Frame(app, bg="#A0C878")
frame_down.pack(side=TOP, pady=25)

# create Table details
columns = ["Amount", "Currency", "Category", "Payment Method", "Date"]
table = ttk.Treeview(frame_down, columns=columns, show='headings', height=10)

# Define column headings
for col in columns:
  table.heading(col, text=col, anchor=CENTER)
  table.column(col, anchor=CENTER)
  
table.grid(row=0, column=0, sticky="nsew")

# Tag styling
table.tag_configure("highlight", background="#A4CCD9", font=("TkDefaultFont 10 bold"))

# Style headers
style = ttk.Style()
style.configure("Treeview.Heading", font=("TkDefaultFont", 10, "bold"), background="red", foreground="#4B70F5")

# Total USD Label
total_usd_label = Label(app, text="💵 Total in USD: 0.00", font=("Arial", 14, "bold"), fg="#E95793", bg="#F0F0F0")
total_usd_label.pack(pady=10)

app.mainloop()