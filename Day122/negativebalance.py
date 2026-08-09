def negativebalance():
    balance = int(input("Enter the initial balance: "))
    transactions = int(input("Enter the number of transactions: "))

    for i in range(1, transactions + 1):
        amount = int(input(f"Enter transaction {i} (+deposit / -withdrawal): "))
        balance += amount

    print("Final Balance:", balance)

    if balance > 0:
        print("Status: Positive Balance")
    elif balance < 0:
        print("Status: Negative Balance")
    else:
        print("Status: Zero Balance")

negativebalance()