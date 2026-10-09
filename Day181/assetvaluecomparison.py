def assetvaluecomparison():
    print("Asset Value Comparison :")

    asset1 = input("Enter first asset name: ")
    value1 = float(input("Enter first asset value: "))

    asset2 = input("Enter second asset name: ")
    value2 = float(input("Enter second asset value: "))

    if value1 < 0 or value2 < 0:
        print("Asset values cannot be negative.")
        return

    difference = abs(value1 - value2)

    print("\nComparison Result :")
    print(asset1, "Value:", round(value1, 2))
    print(asset2, "Value:", round(value2, 2))
    print("Value Difference:", round(difference, 2))

    if value1 > value2:
        print(asset1, "has the higher value.")
    elif value2 > value1:
        print(asset2, "has the higher value.")
    else:
        print("Both assets have equal values.")

    total_value = value1 + value2
    print("Combined Asset Value:", round(total_value, 2))

assetvaluecomparison()