def bankaccountanalyzer():
    balance = float(input("Enter initial bank balance: "))
    deposit = float(input("Enter total deposit amount: "))
    withdrawal = float(input("Enter total withdrawal amount: "))
    interest_rate = float(input("Enter interest rate (%): "))

    if balance < 0 or deposit < 0 or withdrawal < 0 or interest_rate < 0:
        print("Enter valid non-negative values.")
        return

    balance_after_transactions = balance + deposit - withdrawal

    if balance_after_transactions < 0:
        print("Insufficient balance for the given withdrawal.")
        return

    interest = (balance_after_transactions * interest_rate) / 100
    final_balance = balance_after_transactions + interest

    print("\n--- Bank Account Analysis ---")
    print("Initial Balance:", balance)
    print("Total Deposits:", deposit)
    print("Total Withdrawals:", withdrawal)
    print("Balance After Transactions:", balance_after_transactions)
    print("Interest Earned:", interest)
    print("Final Balance:", final_balance)

    if final_balance > balance:
        print("Account Status: Balance Increased")
    elif final_balance < balance:
        print("Account Status: Balance Decreased")
    else:
        print("Account Status: Balance Unchanged")

bankaccountanalyzer()