def sharemarkettransactionmanagement():
    print("Share Market Transaction Management System")

    n = int(input("Enter the number of transactions: "))

    if n <= 0:
        print("Please enter a positive number of transactions.")
        return

    transactions = []
    total_buy = 0
    total_sell = 0

    for i in range(n):
        print(f"\nTransaction {i + 1}")

        stock_name = input("Enter stock name: ")
        transaction_type = input("Enter transaction type (Buy/Sell): ").strip().lower()
        quantity = int(input("Enter quantity of shares: "))
        price = float(input("Enter price per share: "))
        brokerage_rate = float(input("Enter brokerage rate (%): "))

        if transaction_type not in ["buy", "sell"]:
            print("Invalid transaction type.")
            return

        if quantity <= 0 or price <= 0 or brokerage_rate < 0:
            print("Invalid transaction details.")
            return

        amount = quantity * price
        brokerage = amount * brokerage_rate / 100
        total_amount = amount + brokerage if transaction_type == "buy" else amount - brokerage

        if transaction_type == "buy":
            total_buy += total_amount
        else:
            total_sell += total_amount

        transactions.append((stock_name, transaction_type, quantity, price, brokerage, total_amount))

    print("\nShare Market Transaction Report:")
    print(f"{'Stock':<15}{'Type':<10}{'Quantity':<12}{'Price':<12}{'Brokerage':<12}{'Total':<12}")

    for transaction in transactions:
        name, transaction_type, quantity, price, brokerage, total = transaction
        print(f"{name:<15}{transaction_type.title():<10}{quantity:<12}{price:<12.2f}{brokerage:<12.2f}{total:<12.2f}")

    net_amount = total_sell - total_buy

    print("\nTransaction Summary:")
    print("Total Buy Amount:", round(total_buy, 2))
    print("Total Sell Amount:", round(total_sell, 2))
    print("Net Amount:", round(net_amount, 2))

    if net_amount > 0:
        print("Transaction Status: Net Cash Inflow")
    elif net_amount < 0:
        print("Transaction Status: Net Cash Outflow")
    else:
        print("Transaction Status: Balanced")

sharemarkettransactionmanagement()