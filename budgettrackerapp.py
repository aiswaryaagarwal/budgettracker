from flask import Flask, render_template, request, redirect
import json, datetime

app = Flask(__name__)

def save(transactions):
    with open("transactions.json", "w") as f:
        json.dump(transactions, f)

def load():
    try:
        with open("transactions.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route("/")
def home():
    transactions = load()
    credit = sum(t['amount'] for t in transactions if t['type'] == "Credit")
    debit = sum(t['amount'] for t in transactions if t['type'] == "Debit")
    balance = round(credit - debit, 2)
    return render_template("index.html", transactions=transactions, balance=balance)

@app.route("/add", methods=["POST"])
def add():
    transactions = load()
    transactions.append({
        "type": request.form["type"],
        "amount": float(request.form["amount"]),
        "description": request.form["description"],
        "date": str(datetime.date.today())
    })
    save(transactions)
    return redirect("/")


@app.route("/edit/<int:index>")
def edit(index):
    transactions = load()
    transaction = transactions[index]
    return render_template("edit.html", transaction=transaction, index=index)

@app.route("/update/<int:index>", methods=["POST"])
def update(index):
    transactions = load()
    transactions[index]["type"] = request.form["type"]
    transactions[index]["amount"] = float(request.form["amount"])
    transactions[index]["description"] = request.form["description"]
    save(transactions)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    