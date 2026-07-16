def largesttransaction():
    n = int(input("Enter number of transactions: "))
    
    transactions = []
    for i in range(n):
        amount = float(input(f"Enter transaction {i + 1}: "))
        transactions.append(amount)

    print("Largest Transaction =", max(transactions))

largesttransaction()