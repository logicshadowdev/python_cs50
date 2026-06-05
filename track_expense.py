import json
import os

def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

def add_expenses(expenses):
    category = input("Category (food/transport/bills/other): ")
    amount = float(input("Amount: "))
    description = input("Description: ")
    expenses.append({
        "category": category,
        "amount": amount,
        "description": description
    })
    save_expenses(expenses)
    print("Expense added.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    total = 0
    print("\n📊 Your Expenses: \n")
    for e in expenses:
        print(f"{e['category'].upper()}")
        print(f"${e['amount']}")
        print(f"{e['description']}")
        print("-" * 30)
        total += e['amount']
    print(f"Total Spent: ${total}")

expenses = load_expenses()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Quit")

    choice = input("\nChoose: ")

    if choice == "1":
        add_expenses(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        break
    else:
        print("Invalid choice")
