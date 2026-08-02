def businesstransaction():
    balance = float(input("Enter the initial balance: "))
    transaction = input("Enter transaction type (deposit/withdraw): ").lower()
    amount = float(input("Enter the transaction amount: "))

    if transaction == "deposit":
        balance += amount
        print("Amount Deposited:", amount)
    elif transaction == "withdraw":
        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")
            return
    else:
        print("Invalid Transaction Type")
        return

    print("Current Balance:", round(balance, 2))

businesstransaction()