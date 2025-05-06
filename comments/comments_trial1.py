import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#creating a class to override the functions
class Child:
    '''making a def with init, and objects named self, name and setting 
    balance equal to 300'''
    def __init__(self, name, balance=300):
        self.name = name
        self.balance = balance #whenever self.balance is present, 300 is called
        self.bonus_qualify = False

    def spend_money(self, amount): #eg from comment on line 11
        if self.balance >= amount:
            self.balance -= amount
        else: #error message
            print(f"{self} does not have enough money for ${amount} purchase")

    def check_bonus(self):
        self.bonus_qualify = self.balance >= 50 #if the child's balance is above $50, bonus_qualify set to True

    def get_info(self):
        self.check_bonus()
        return self.balance, self.bonus_qualify

#creating a dictionary for the selfren, the initial balance, and qualifying for bonus set as false
children_data = { 
    '''making a dictionary for each child, using the class "Child"
    to link them together'''
    "Nikau": Child("Nikau"),
    "Hana": Child("Hana"),
    "Tia": Child("Tia")
}

#creating a GUI

def create_gui():
    '''making the main root'''
    root = tk.Tk()
    root.title("Child Spending Tracker")
    root.geometry("400x300")

    #making a drop down for the children

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

    #button to spend money
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