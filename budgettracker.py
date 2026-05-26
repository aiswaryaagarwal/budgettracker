import json
import datetime
def save(transactions):
    with open("transactions.json", "w") as f:
        json.dump(transactions, f)
def load():
    try:
        with open("transactions.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
transactions=[]
transactions = load()
while True:
    print("\n")
    print("--Budget Tracker--")
    print("1. Credit amount")
    print("2. Debit amount")
    print("3. View Transactions")
    print("4. Show Balance")
    print("5. Quit")
    n = input("Choose an option:")
    if n=='1':
        amount = float(input("Enter credit amount:"))
        description = input("Enter description:")
        date = str(datetime.date.today())
        transactions.append({"type": "Credit", "amount": amount, "date": date, "description": description})
        save(transactions)
    elif n=='2':
        amount = float(input("Enter debit amount:"))
        description = input("Enter description:")
        date = str(datetime.date.today())
        transactions.append({"type": "Debit", "amount": amount, "date": date, "description": description})
        save(transactions)
    elif n=='3':
        print("Transactions:")
        for transaction in transactions:
            print(f"- {transaction['type']}: Rs.{transaction['amount']:.2f} ({transaction['date']}) - {transaction['description']}")
    elif n=='4':
        print("Current Balance:")
        balance = sum(transaction['amount'] for transaction in transactions if transaction['type'] == "Credit") - sum(transaction['amount'] for transaction in transactions if transaction['type'] == "Debit")
        print(f"Rs.{balance:.2f}")
    elif n=='5':
        print("Exiting Budget Tracker. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option.")
