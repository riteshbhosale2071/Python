def businesstransactionanalyzer():
    print("Business Transaction Analyzer :")

    number_of_transactions = int(input("Enter number of transactions: "))

    if number_of_transactions <= 0:
        print("Enter a valid number of transactions.")
        return

    transactions = []
    total_income = 0
    total_expense = 0

    for i in range(number_of_transactions):
        print("\nTransaction", i + 1)

        transaction_type = input("Enter type (income/expense): ").lower()
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if transaction_type == "income":
            total_income += amount
            transactions.append(["Income", amount])
        elif transaction_type == "expense":
            total_expense += amount
            transactions.append(["Expense", amount])
        else:
            print("Enter either income or expense.")
            return

    profit_or_loss = total_income - total_expense

    print("\nTransaction Summary :")

    for i in range(len(transactions)):
        print("Transaction", i + 1, ":", transactions[i][0], "-", round(transactions[i][1], 2))

    print("\nTotal Income:", round(total_income, 2))
    print("Total Expense:", round(total_expense, 2))
    print("Net Result:", round(profit_or_loss, 2))

    if profit_or_loss > 0:
        print("Business Status: Profit")
    elif profit_or_loss < 0:
        print("Business Status: Loss")
    else:
        print("Business Status: Break-even")

    if total_income > 0:
        profit_margin = (profit_or_loss / total_income) * 100
        print("Profit Margin:", round(profit_margin, 2), "%")

businesstransactionanalyzer()