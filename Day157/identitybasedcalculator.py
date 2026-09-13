def identitybasedcalculator():
    print("Identity-Based Calculator :")
    print("1. (a + b)^2")
    print("2. (a - b)^2")
    print("3. a^2 - b^2")
    print("4. (a + b)^3")
    print("5. (a - b)^3")

    choice = int(input("Enter identity number: "))
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))

    if choice == 1:
        result = a * a + 2 * a * b + b * b
        print("Result:", result)

    elif choice == 2:
        result = a * a - 2 * a * b + b * b
        print("Result:", result)

    elif choice == 3:
        result = (a + b) * (a - b)
        print("Result:", result)

    elif choice == 4:
        result = a * a * a + 3 * a * a * b + 3 * a * b * b + b * b * b
        print("Result:", result)

    elif choice == 5:
        result = a * a * a - 3 * a * a * b + 3 * a * b * b - b * b * b
        print("Result:", result)

    else:
        print("Invalid identity number.")

identitybasedcalculator()