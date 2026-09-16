def variationtypeclassifier():
    print("Variation Type Classifier :")
    print("1. Direct Variation")
    print("2. Inverse Variation")

    choice = int(input("Enter choice: "))

    x1 = float(input("Enter first x value: "))
    y1 = float(input("Enter first y value: "))
    x2 = float(input("Enter second x value: "))
    y2 = float(input("Enter second y value: "))

    if choice == 1:
        if x1 != 0 and x2 != 0:
            k1 = y1 / x1
            k2 = y2 / x2

            if k1 == k2:
                print("The data shows Direct Variation.")
            else:
                print("The data does not show Direct Variation.")
        else:
            print("x cannot be zero.")

    elif choice == 2:
        k1 = x1 * y1
        k2 = x2 * y2

        if k1 == k2:
            print("The data shows Inverse Variation.")
        else:
            print("The data does not show Inverse Variation.")

    else:
        print("Invalid choice.")

variationtypeclassifier()