def variationgraphdata():
    print("Variation Graph Data Generator :")
    print("1. Direct Variation")
    print("2. Inverse Variation")

    choice = int(input("Enter choice: "))
    k = float(input("Enter variation constant k: "))
    n = int(input("Enter number of x values: "))

    print("x\t\ty")

    for i in range(n):
        x = float(input("Enter x value: "))

        if choice == 1:
            y = k * x
            print(x, "\t\t", y)

        elif choice == 2:
            if x != 0:
                y = k / x
                print(x, "\t\t", y)
            else:
                print("x cannot be zero.")

        else:
            print("Invalid choice.")
            break

variationgraphdata()