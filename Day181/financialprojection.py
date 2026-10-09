def financialprojection():
    print("Financial Projection :")

    initial_amount = float(input("Enter initial amount: "))
    annual_income = float(input("Enter expected annual income: "))
    annual_expenses = float(input("Enter expected annual expenses: "))
    growth_rate = float(input("Enter annual income growth rate (%): "))
    expense_rate = float(input("Enter annual expense growth rate (%): "))
    years = int(input("Enter projection period in years: "))

    if initial_amount < 0 or annual_income < 0 or annual_expenses < 0:
        print("Amounts cannot be negative.")
        return

    if growth_rate < 0 or expense_rate < 0 or years <= 0:
        print("Enter valid growth rates and number of years.")
        return

    balance = initial_amount
    income = annual_income
    expenses = annual_expenses
    total_income = 0
    total_expenses = 0

    print("\nYear\tIncome\t\tExpenses\tNet Savings\tBalance")

    for year in range(1, years + 1):
        income = income * (1 + growth_rate / 100)
        expenses = expenses * (1 + expense_rate / 100)

        savings = income - expenses
        balance += savings

        total_income += income
        total_expenses += expenses

        print(year, "\t", round(income, 2), "\t",
              round(expenses, 2), "\t\t",
              round(savings, 2), "\t\t", round(balance, 2))

    print("\nFinancial Projection Summary :")
    print("Initial Balance:", round(initial_amount, 2))
    print("Total Projected Income:", round(total_income, 2))
    print("Total Projected Expenses:", round(total_expenses, 2))
    print("Total Net Savings:", round(total_income - total_expenses, 2))
    print("Final Balance:", round(balance, 2))

    if balance > initial_amount:
        print("Financial Status: Balance increased.")
    elif balance < initial_amount:
        print("Financial Status: Balance decreased.")
    else:
        print("Financial Status: Balance remained unchanged.")

financialprojection()