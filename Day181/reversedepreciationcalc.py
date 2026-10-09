def reversedepreciationcalc():
    print("Reverse Depreciation Calculator :")

    final_value = float(input("Enter current asset value: "))
    rate = float(input("Enter annual depreciation rate (%): "))
    years = int(input("Enter number of years: "))

    if final_value <= 0 or rate <= 0 or rate >= 100 or years <= 0:
        print("Enter valid values.")
        return

    initial_value = final_value / ((1 - rate / 100) ** years)
    total_depreciation = initial_value - final_value
    depreciation_percentage = (total_depreciation / initial_value) * 100

    print("\nDepreciation Results :")
    print("Current Asset Value:", round(final_value, 2))
    print("Original Asset Value:", round(initial_value, 2))
    print("Total Depreciation:", round(total_depreciation, 2))
    print("Overall Depreciation:", round(depreciation_percentage, 2), "%")

reversedepreciationcalc()