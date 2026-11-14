def financialtransactionmanager():
    transactions = []

    while True:
        print("\nFinancial Transaction Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Calculate Total Income")
        print("5. Calculate Total Expenses")
        print("6. View Account Balance")
        print("7. Search Transactions")
        print("8. Delete Transaction")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice in ["1", "2"]:
            try:
                transaction_type = "Income" if choice == "1" else "Expense"
                amount = float(input("Enter amount (₹): "))
                category = input("Enter category: ")
                description = input("Enter description: ")

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                transactions.append({
                    "type": transaction_type,
                    "amount": amount,
                    "category": category,
                    "description": description
                })

                print(transaction_type, "transaction added successfully.")

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":
            if not transactions:
                print("No transactions available.")
            else:
                print("\nTransaction History")
                for i, transaction in enumerate(transactions, 1):
                    print(f"\nTransaction {i}")
                    print("Type:", transaction["type"])
                    print("Amount: ₹", round(transaction["amount"], 2))
                    print("Category:", transaction["category"])
                    print("Description:", transaction["description"])

        elif choice == "4":
            total_income = sum(
                t["amount"] for t in transactions
                if t["type"] == "Income"
            )
            print("Total Income: ₹", round(total_income, 2))

        elif choice == "5":
            total_expenses = sum(
                t["amount"] for t in transactions
                if t["type"] == "Expense"
            )
            print("Total Expenses: ₹", round(total_expenses, 2))

        elif choice == "6":
            income = sum(
                t["amount"] for t in transactions
                if t["type"] == "Income"
            )
            expenses = sum(
                t["amount"] for t in transactions
                if t["type"] == "Expense"
            )

            balance = income - expenses
            print("Account Balance: ₹", round(balance, 2))

        elif choice == "7":
            keyword = input("Enter category or description to search: ").lower()

            results = [
                t for t in transactions
                if keyword in t["category"].lower()
                or keyword in t["description"].lower()
            ]

            if results:
                print("\nMatching Transactions:")
                for transaction in results:
                    print(
                        transaction["type"],
                        "| ₹", round(transaction["amount"], 2),
                        "|", transaction["category"],
                        "|", transaction["description"]
                    )
            else:
                print("No matching transactions found.")

        elif choice == "8":
            try:
                transaction_number = int(input("Enter transaction number to delete: "))

                if 1 <= transaction_number <= len(transactions):
                    removed = transactions.pop(transaction_number - 1)
                    print("Deleted transaction:", removed["description"])
                else:
                    print("Invalid transaction number.")

            except ValueError:
                print("Please enter a valid transaction number.")

        elif choice == "0":
            print("Thank you for using Financial Transaction Manager!")
            break

        else:
            print("Invalid choice. Please try again.")

financialtransactionmanager()