def identityoptimization():
    print("Identity Optimization Program :")
    print("1. Square of Sum")
    print("2. Square of Difference")
    print("3. Difference of Squares")

    choice = int(input("Choose an identity: "))

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    if choice == 1:
        result = a * a + 2 * a * b + b * b
        print("Optimized calculation using (a + b)^2")
        print("Result =", result)

    elif choice == 2:
        result = a * a - 2 * a * b + b * b
        print("Optimized calculation using (a - b)^2")
        print("Result =", result)

    elif choice == 3:
        result = (a + b) * (a - b)
        print("Optimized calculation using a^2 - b^2")
        print("Result =", result)

    else:
        print("Invalid choice.")

identityoptimization()