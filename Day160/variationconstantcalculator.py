def variationconstantcalculator():
    print("Variation Constant Calculator :")
    print("1. Direct Variation: y = kx")
    print("2. Inverse Variation: y = k/x")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = float(input("Enter value of x: "))
        y = float(input("Enter value of y: "))

        if x != 0:
            k = y / x
            print("Variation constant k =", k)
        else:
            print("x cannot be zero.")

    elif choice == 2:
        x = float(input("Enter value of x: "))
        y = float(input("Enter value of y: "))

        if x != 0:
            k = x * y
            print("Variation constant k =", k)
        else:
            print("x cannot be zero.")

    else:
        print("Invalid choice.")

variationconstantcalculator()