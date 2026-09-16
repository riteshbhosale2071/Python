def variationdatavalidator():
    print("Variation Data Validator :")
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

    valid = True

    if choice == 1:
        if x_values[0] == 0:
            valid = False
        else:
            constant = y_values[0] / x_values[0]

            for i in range(1, n):
                if x_values[i] == 0 or y_values[i] / x_values[i] != constant:
                    valid = False
                    break

    elif choice == 2:
        constant = x_values[0] * y_values[0]

        for i in range(1, n):
            if x_values[i] * y_values[i] != constant:
                valid = False
                break

    else:
        print("Invalid choice.")
        return

    if valid:
        print("The data is valid for the selected variation.")
    else:
        print("The data is not valid for the selected variation.")

variationdatavalidator()