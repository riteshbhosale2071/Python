def savingsgrowth():
    initial_savings = float(input("Enter the initial savings: "))
    monthly_saving = float(input("Enter the monthly saving amount: "))
    months = int(input("Enter the number of months: "))

    total_savings = initial_savings + (monthly_saving * months)

    print("Initial Savings:", round(initial_savings, 2))
    print("Monthly Saving:", round(monthly_saving, 2))
    print("Total Savings after", months, "months:", round(total_savings, 2))

savingsgrowth()