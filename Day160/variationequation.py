def variationequation():
    print("Variation Equation Generator :")
    print("1. Direct Variation: y = kx")
    print("2. Inverse Variation: y = k/x")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = float(input("Enter value of x: "))
        y = float(input("Enter value of y: "))

        if x != 0:
            k = y / x
            print("Variation equation: y =", k, "x")
        else:
            print("x cannot be zero.")

    elif choice == 2:
        x = float(input("Enter value of x: "))
        y = float(input("Enter value of y: "))

        if x != 0:
            k = x * y
            print("Variation equation: y =", k, "/ x")
        else:
            print("x cannot be zero.")

    else:
        print("Invalid choice.")

variationequation()