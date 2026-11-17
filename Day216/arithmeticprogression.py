def arithmeticprogression():
    print("Arithmetic Progression Financial Planner")

    first_saving = float(input("Enter first month's savings: "))
    increase = float(input("Enter monthly increase in savings: "))
    months = int(input("Enter number of months: "))

    if first_saving < 0 or increase < 0 or months <= 0:
        print("Please enter valid positive values.")
        return

    total_savings = 0

    print("\nMonthly Savings Plan:")
    print(f"{'Month':<15}{'Savings':<15}{'Total Savings':<15}")

    for month in range(1, months + 1):
        saving = first_saving + (month - 1) * increase
        total_savings += saving

        print(f"{month:<15}{saving:<15.2f}{total_savings:<15.2f}")

    print("\nFinancial Planning Summary:")
    print("First Month Savings:", first_saving)
    print("Monthly Increase:", increase)
    print("Number of Months:", months)
    print("Last Month Savings:", first_saving + (months - 1) * increase)
    print("Total Savings:", round(total_savings, 2))
    print("Average Monthly Savings:", round(total_savings / months, 2))

arithmeticprogression()