def growthvsdepreciation():
    print("Growth vs Depreciation Simulator :")

    initial_value = float(input("Enter initial amount: "))
    growth_rate = float(input("Enter annual growth rate (%): "))
    depreciation_rate = float(input("Enter annual depreciation rate (%): "))
    years = int(input("Enter number of years: "))

    if initial_value <= 0 or growth_rate < 0 or depreciation_rate < 0 or depreciation_rate > 100 or years <= 0:
        print("Enter valid values.")
        return

    growth_value = initial_value
    depreciation_value = initial_value

    print("\nYear\tGrowth Value\tDepreciated Value\tDifference")

    for year in range(1, years + 1):
        growth_value = growth_value * (1 + growth_rate / 100)
        depreciation_value = depreciation_value * (1 - depreciation_rate / 100)
        difference = growth_value - depreciation_value

        print(year, "\t", round(growth_value, 2), "\t\t", round(depreciation_value, 2), "\t\t", round(difference, 2))

    print("\nFinal Comparison :")
    print("Initial Amount:", round(initial_value, 2))
    print("Final Growth Value:", round(growth_value, 2))
    print("Final Depreciated Value:", round(depreciation_value, 2))
    print("Final Difference:", round(growth_value - depreciation_value, 2))

growthvsdepreciation()