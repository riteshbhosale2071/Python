def proportionaldatavalidator():
    n = int(input("Enter the number of data pairs: "))

    if n < 2:
        print("Enter at least 2 data pairs.")
        return

    x_values = []
    y_values = []

    for i in range(n):
        print(f"\nData Pair {i + 1}:")
        x = float(input("Enter X: "))
        y = float(input("Enter Y: "))

        if x == 0:
            print("X cannot be zero.")
            return

        x_values.append(x)
        y_values.append(y)

    constant_ratio = y_values[0] / x_values[0]
    proportional = True

    for i in range(1, n):
        ratio = y_values[i] / x_values[i]

        if ratio != constant_ratio:
            proportional = False
            break

    print("\nProportional Data Validation :")
    print("Common Ratio:", constant_ratio)

    if proportional:
        print("The data is Proportional.")
        print("Y is directly proportional to X.")
    else:
        print("The data is Not Proportional.")

proportionaldatavalidator()