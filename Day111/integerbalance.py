def integerbalance():
    balance = int(input("Enter the starting balance: "))
    change = int(input("Enter the balance change (+ for deposit, - for withdrawal): "))

    final_balance = balance + change

    print("Final Balance:", final_balance)

integerbalance()