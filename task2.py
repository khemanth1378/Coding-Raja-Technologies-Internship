import tkinter as tk
from tkinter import messagebox

budget = {
    "Income": 0,
    "Expenses": 0,
    "Balance": 0
}

def update_balance():
    income = float(income_entry.get())
    expenses = float(expenses_entry.get())
    
    budget["Income"] = income
    budget["Expenses"] = expenses
    budget["Balance"] = income - expenses
    
    balance_label.config(text=f"Balance: ${budget['Balance']:.2f}")

root = tk.Tk()
root.title("Personal Budget Tracker")

income_label = tk.Label(root, text="Income:",width=30,bg='pink')
income_label.pack()
income_entry = tk.Entry(root)
income_entry.pack()

expenses_label = tk.Label(root, text="Expenses:",width=30,bg='skyblue')
expenses_label.pack()
expenses_entry = tk.Entry(root)
expenses_entry.pack()

update_button = tk.Button(root, text="Update Balance", command=update_balance,width=30,bg='orange')
update_button.pack()

balance_label = tk.Label(root, text="Balance: $0.00")
balance_label.pack()

root.mainloop()
