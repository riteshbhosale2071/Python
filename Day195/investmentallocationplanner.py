def investmentallocationplanner():
    print("Investment Allocation Planner :")

    try:
        total_amount = float(input("Enter your total investment amount: "))
        n = int(input("Enter the number of investment options: "))
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    if total_amount <= 0:
        print("Investment amount must be greater than zero.")
        return

    if n <= 0:
        print("Number of investment options must be greater than zero.")
        return

    investments = []
    percentages = []

    print("\nEnter investment options and allocation percentages.")

    for i in range(n):
        name = input("\nEnter investment option " + str(i + 1) + ": ")

        try:
            percentage = float(input("Enter allocation percentage: "))
        except ValueError:
            print("Invalid percentage! Please enter a numeric value.")
            return

        if percentage < 0 or percentage > 100:
            print("Allocation percentage must be between 0 and 100.")
            return

        investments.append(name)
        percentages.append(percentage)

    total_percentage = sum(percentages)

    print("\nAllocation Summary :")
    print("Total Investment Amount:", round(total_amount, 2))
    print("Total Allocation Percentage:", round(total_percentage, 2), "%")

    if total_percentage > 100:
        print("Warning: Allocation exceeds 100%.")
        print("Please adjust the percentages before investing.")
    elif total_percentage < 100:
        print("Note: Some investment amount remains unallocated.")
    else:
        print("Allocation percentages total 100%.")

    print("\nInvestment Distribution :")
    print("{:<25}{:<15}{:<15}".format(
        "Investment", "Percentage", "Amount"
    ))
    print("-" * 55)

    allocated_amount = 0

    for i in range(n):
        amount = total_amount * percentages[i] / 100
        allocated_amount += amount

        print("{:<25}{:<15.2f}{:<15.2f}".format(
            investments[i], percentages[i], amount
        ))

    unallocated_amount = total_amount - allocated_amount

    print("-" * 55)
    print("Total Allocated Amount:", round(allocated_amount, 2))
    print("Unallocated Amount:", round(unallocated_amount, 2))

    print("\nAllocation Analysis :")

    largest_index = percentages.index(max(percentages))
    smallest_index = percentages.index(min(percentages))

    print("Largest Allocation:", investments[largest_index])
    print("Largest Percentage:", percentages[largest_index], "%")

    print("Smallest Allocation:", investments[smallest_index])
    print("Smallest Percentage:", percentages[smallest_index], "%")

    if total_percentage == 100:
        print("\nStatus: Investment plan is fully allocated.")
    elif total_percentage < 100:
        print("\nStatus: Investment plan is partially allocated.")
    else:
        print("\nStatus: Investment plan exceeds the available amount.")

    print("\nVerification :")
    print("Sum of Allocation Percentages:", round(sum(percentages), 2), "%")
    print("Sum of Investment Amounts:", round(allocated_amount, 2))

    if abs(allocated_amount - total_amount) < 0.01 and total_percentage == 100:
        print("Verification successful: All funds are allocated.")
    else:
        print("Review the percentages to complete the allocation.")

    print("\nNote: This planner calculates allocation amounts only.")
    print("It does not predict returns or assess investment risk.")

investmentallocationplanner()