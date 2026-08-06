def monthlyexpense():
    income = float(input("Enter your monthly income: "))
    expense = float(input("Enter your total monthly expenses: "))

    savings = income - expense

    print("Monthly Income:", income)
    print("Monthly Expenses:", expense)
    print("Savings:", savings)

    if savings > 0:
        print("You saved money this month.")
    elif savings == 0:
        print("No savings this month.")
    else:
        print("You spent more than your income.")

monthlyexpense()