def variationrulediscovery():
    print("Variation Rule Discovery Program :")
    print("1. Direct Variation")
    print("2. Inverse Variation")

    choice = int(input("Enter choice: "))
    n = int(input("Enter number of data pairs: "))

    x_values = []
    y_values = []

    for i in range(n):
        x = float(input("Enter x value: "))
        y = float(input("Enter y value: "))
        x_values.append(x)
        y_values.append(y)

    if choice == 1:
        if x_values[0] != 0:
            k = y_values[0] / x_values[0]
            valid = True

            for i in range(1, n):
                if x_values[i] == 0 or y_values[i] / x_values[i] != k:
                    valid = False
                    break

            if valid:
                print("Direct variation rule discovered.")
                print("y =", k, "x")
            else:
                print("No direct variation rule found.")
        else:
            print("x cannot be zero.")

    elif choice == 2:
        k = x_values[0] * y_values[0]
        valid = True

        for i in range(1, n):
            if x_values[i] * y_values[i] != k:
                valid = False
                break

        if valid:
            print("Inverse variation rule discovered.")
            print("y =", k, "/ x")
        else:
            print("No inverse variation rule found.")

    else:
        print("Invalid choice.")

variationrulediscovery()