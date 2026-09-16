def variationoutlierdetector():
    print("Variation Outlier Detector :")
    print("1. Direct Variation")
    print("2. Inverse Variation")

    choice = int(input("Enter variation type: "))
    n = int(input("Enter number of data pairs: "))

    x_values = []
    y_values = []

    for i in range(n):
        x = float(input("Enter x value: "))
        y = float(input("Enter y value: "))
        x_values.append(x)
        y_values.append(y)

    if choice == 1:
        constants = []

        for i in range(n):
            if x_values[i] != 0:
                constants.append(y_values[i] / x_values[i])

        average = sum(constants) / len(constants)

        print("Outliers:")

        found = False

        for i in range(n):
            if x_values[i] != 0:
                k = y_values[i] / x_values[i]

                if k != average:
                    print("x =", x_values[i], ", y =", y_values[i])
                    found = True

        if not found:
            print("No outliers found.")

    elif choice == 2:
        constants = []

        for i in range(n):
            constants.append(x_values[i] * y_values[i])

        average = sum(constants) / len(constants)

        print("Outliers:")

        found = False

        for i in range(n):
            k = x_values[i] * y_values[i]

            if k != average:
                print("x =", x_values[i], ", y =", y_values[i])
                found = True

        if not found:
            print("No outliers found.")

    else:
        print("Invalid choice.")

variationoutlierdetector()