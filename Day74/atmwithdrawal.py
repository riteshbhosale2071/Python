def atm():
    balance = float(input("Enter account balance: ₹"))
    withdraw = float(input("Enter withdrawal amount: ₹"))

    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawal Successful")
        print("Remaining Balance = ₹", balance)
    else:
        print("Insufficient Balance")

atm()