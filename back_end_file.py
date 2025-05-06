import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

#creating a dictionary for the children, the initial balance, and qualifying for bonus
children = {
    "Nikau":{"balance":300, "bonus_qualify":False},
    "Hana":{"balance":300, "bonus_qualify":False},
    "Tia":{"balance":300, "bonus_qualify":False}
}

def spend_money(child_name, amount):
    '''creating a def where 
the money is deducted from the balance. 
The amount is underneath, each child spending is 
different. From the initial balance of 300, the unique 
amount is deducted'''
    if child_name in children:
        if children[child_name]["balance"]>=amount:
            children[child_name]["balance"]-=amount
        else:
            print(f"{child_name} does not have enough money for ${amount} transaction ")

def check_bonus(child_name):
    if child_name in children:
        if children[child_name]["balance"] >= 50:
            children[child_name]["bonus_qualify"] = True
        else:
            children[child_name]["bonus_qualify"] = False

def get_child_info(child_name):
    balance = children[child_name]["balance"]
    bonus = children[child_name]["bonus_qualify"]
    print(f"{child_name} has ${balance} remaining")
    return balance, check_bonus

#creating a GUI

def create_gui():
    root = tk.Tk()
    root.title("Child Spending Tracker")
    root.geometry("400x300")

    #making a drop down for the children

    tk.Label(root, text="Select Child:").pack(pady=5)
    child_var = tk.StringVar(value="Nikau")
    child_menu = ttk.Combobox(root, textvariable=child_var, values=list(children.keys()), state="readonly")
    child_menu.pack()

    #enter amount to spend
    tk.Label(root, text="Enter amount to spend:").pack(pady=5)
    spend_amount = tk.StringVar()
    amount_entry = tk.Entry(root, textvariable=spend_amount)
    amount_entry.pack()

    #display area
    display = tk.Label(root, text="", font=("Arial", 12), pady=10)
    display.pack()

    def update_display():
        name = child_var.get()
        balance, bonus = get_child_info(name)
        status = "qualifies for the bonus" if bonus else "does NOT qualify for bonus"
        display.config(text=f"{name} has ${balance}\n{name} {status}")

    #Button to spend money
    def spend():
        name = child_var.get()
        try:
            amt = float(spend_amount.get())
            spend_money(name, amt)
            check_bonus(name)
            update_display()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
    spend_btn = tk.Button(root, text="Spend Money", command=spend)
    spend_btn.pack(pady=10)
    
    root.mainloop()

create_gui()