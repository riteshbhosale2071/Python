def fastcalculationusingidentities():
    print("Fast Calculation Using Identities :")
    print("1. Calculate (a + b)^2")
    print("2. Calculate (a - b)^2")
    print("3. Calculate a^2 - b^2")
    print("4. Calculate (a + b)(a - b)")

    choice = int(input("Enter choice: "))
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    if choice == 1:
        result = a * a + 2 * a * b + b * b
        print("(a + b)^2 =", result)

    elif choice == 2:
        result = a * a - 2 * a * b + b * b
        print("(a - b)^2 =", result)

    elif choice == 3:
        result = (a + b) * (a - b)
        print("a^2 - b^2 =", result)

    elif choice == 4:
        result = a * a - b * b
        print("(a + b)(a - b) =", result)

    else:
        print("Invalid choice.")

fastcalculationusingidentities()