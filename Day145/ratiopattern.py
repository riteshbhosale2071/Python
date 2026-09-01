def ratiopattern():
    n = int(input("Enter the number of values: "))

    if n < 2:
        print("Enter at least 2 values.")
        return

    values = []

    for i in range(n):
        value = float(input(f"Enter value {i + 1}: "))

        if value == 0:
            print("Values must be non-zero.")
            return

        values.append(value)

    ratio = values[1] / values[0]
    is_geometric = True

    for i in range(2, n):
        current_ratio = values[i] / values[i - 1]

        if current_ratio != ratio:
            is_geometric = False
            break

    print("\nRatio Pattern Analysis :")

    if is_geometric:
        print("A constant ratio pattern is detected.")
        print("Common Ratio:", ratio)
    else:
        print("No constant ratio pattern detected.")

ratiopattern()