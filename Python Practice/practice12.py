import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

DATA_FILE = 'data.json'

# Load data from file
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Calculate balance
def calculate_balance(data):
    income = sum(t['amount'] for t in data if t['type'] == 'Income')
    expense = sum(t['amount'] for t in data if t['type'] == 'Expense')
    return income - expense, income, expense

# Add transaction logic
def add_transaction():
    try:
        t_type = type_var.get()
        amount = float(amount_entry.get())
        desc = desc_entry.get()

        if not desc:
            messagebox.showwarning("Input Error", "Please enter a description.")
            return

        transaction = {"type": t_type, "amount": amount, "description": desc}
        data.append(transaction)
        save_data(data)

        update_ui()
        amount_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")

# Update UI elements
def update_ui():
    balance, income, expense = calculate_balance(data)
    balance_label.config(text=f"💰 Balance: ₹{balance:.2f} (Income: ₹{income:.2f}, Expense: ₹{expense:.2f})")

    transaction_list.delete(0, tk.END)
    for t in data:
        transaction_list.insert(tk.END, f"[{t['type']}] ₹{t['amount']} - {t['description']}")

# --- GUI Setup ---

data = load_data()

root = tk.Tk()
root.title("Personal Budget Tracker")
root.geometry("500x550")
root.resizable(False, False) 

# Title
title = tk.Label(root, text="📝 Budget Tracker", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Type dropdown
type_var = tk.StringVar(value="Expense")
type_dropdown = ttk.Combobox(input_frame, textvariable=type_var, values=["Income", "Expense"], state="readonly", width=10)
type_dropdown.grid(row=0, column=0, padx=5)

# Amount
amount_entry = tk.Entry(input_frame, width=15)
amount_entry.grid(row=0, column=1, padx=5)
amount_entry.insert(0, "0.00")

# Description
desc_entry = tk.Entry(input_frame, width=25)
desc_entry.grid(row=0, column=2, padx=5)
desc_entry.insert(0, "Description")

# Add Button
add_btn = tk.Button(root, text="Add Transaction", command=add_transaction, bg="#4ade80", fg="black", width=30)
add_btn.pack(pady=10)

# Balance
balance_label = tk.Label(root, text="Balance: ₹0.00", font=("Helvetica", 14), fg="blue")
balance_label.pack(pady=5)

# Transaction List
transaction_list = tk.Listbox(root, width=60, height=15)
transaction_list.pack(pady=10)

# Initial UI update
update_ui()

# Start GUI loop
root.mainloop()
