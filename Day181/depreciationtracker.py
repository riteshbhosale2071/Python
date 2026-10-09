def depreciationtracker():
    print("Depreciation Tracker :")

    initial_value = float(input("Enter initial asset value: "))
    rate = float(input("Enter annual depreciation rate (%): "))
    years = int(input("Enter number of years: "))

    if initial_value <= 0 or rate < 0 or rate > 100 or years <= 0:
        print("Enter valid values.")
        return

    current_value = initial_value
    total_depreciation = 0

    print("\nYear\tDepreciation\tRemaining Value")

    for year in range(1, years + 1):
        depreciation = current_value * rate / 100
        current_value -= depreciation
        total_depreciation += depreciation

        print(year, "\t", round(depreciation, 2), "\t\t", round(current_value, 2))

    print("\nDepreciation Summary :")
    print("Initial Asset Value:", round(initial_value, 2))
    print("Total Depreciation:", round(total_depreciation, 2))
    print("Remaining Asset Value:", round(current_value, 2))

    if current_value < initial_value:
        print("Asset Value Status: Depreciated")

depreciationtracker()