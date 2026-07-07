def feedexpense():
    animals = int(input("Enter number of animals: "))
    feed_cost = float(input("Enter feed cost per animal: "))

    total_expense = animals * feed_cost

    print("Total Feed Expense:", total_expense)

feedexpense()