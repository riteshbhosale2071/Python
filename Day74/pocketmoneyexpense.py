def pocket():
    pocket_money = float(input("Enter pocket money received: ₹"))

    expenses = float(input("Enter total expenses: ₹"))

    remaining = pocket_money - expenses

    print("Pocket Money = ₹", pocket_money)
    print("Expenses = ₹", expenses)
    print("Remaining Money = ₹", remaining)

pocket()