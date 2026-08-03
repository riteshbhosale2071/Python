def bankingtransaction():
    balance = float(input("Enter your initial account balance: "))

    print("\n1. Deposit")
    print("2. Withdraw")
    choice = int(input("Enter your choice (1 or 2): "))

    amount = float(input("Enter the transaction amount: "))

    if choice == 1:
        balance += amount
        print("Deposit Successful!")
    elif choice == 2:
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance!")
            return
    else:
        print("Invalid Choice!")
        return

    print("Current Balance:", round(balance, 2))

bankingtransaction()