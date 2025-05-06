import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Child:
    def __init__(self, name, balance=300):
        self.name = name
        self.balance = balance
        self.bonus_qualify = False

    def spend_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"{self} does not have enough money for ${amount} purchase")

    def check_bonus(self):
        self.bonus_qualify = self.balance >= 50

    def get_info(self):
        self.check_bonus()
        return self.balance, self.bonus_qualify

#creating a dictionary for the selfren, the initial balance, and qualifying for bonus set as false
children_data = {
    "Nikau": Child("Nikau"),
    "Hana": Child("Hana"),
    "Tia": Child("Tia")
}

#creating a GUI

def create_gui():
    root = tk.Tk()
    root.title("Child Spending Tracker")
    root.geometry("400x300")

    #making a drop down for the selfren

    tk.Label(root, text="Select child:").pack(pady=5)
    child_var = tk.StringVar(value="Nikau")
    child_menu = ttk.Combobox(root, textvariable=child_var, values=list(children_data.keys()), state="readonly")
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
        child = children_data[name]
        balance, bonus = child.get_info()
        status = "qualifies for the bonus" if bonus else "does NOT qualify for bonus"
        display.config(text=f"{name} has ${balance}\n{name} {status}")

    #Button to spend money
    def spend():
        name = child_var.get()
        child = children_data[name]
        try:
            amt = float(spend_amount.get())
            child.spend_money(amt)
            child.check_bonus()
            update_display()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
    spend_btn = tk.Button(root, text="Spend Money", command=spend)
    spend_btn.pack(pady=10)
    
    update_display()
    root.mainloop()

create_gui()