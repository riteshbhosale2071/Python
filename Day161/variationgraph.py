def variationgraph():
    print("Variation Graph Data Generator :")
    print("1. Direct Variation")
    print("2. Inverse Variation")

    choice = int(input("Enter choice: "))
    k = float(input("Enter variation constant k: "))
    n = int(input("Enter number of data points: "))

    x_values = []
    y_values = []

    for i in range(n):
        x = float(input("Enter x value: "))

        if choice == 1:
            y = k * x
            x_values.append(x)
            y_values.append(y)

        elif choice == 2:
            if x != 0:
                y = k / x
                x_values.append(x)
                y_values.append(y)
            else:
                print("x cannot be zero.")
        else:
            print("Invalid choice.")
            return

    print("Graph Data:")
    print("x\t\ty")

    for i in range(len(x_values)):
        print(x_values[i], "\t\t", y_values[i])

variationgraph()