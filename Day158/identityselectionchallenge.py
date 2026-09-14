def identityselectionchallenge():
    print("Identity Selection Challenge :")
    print("1. (a + b)^2")
    print("2. (a - b)^2")
    print("3. a^2 - b^2")
    print("4. (a + b)^3")
    print("5. (a - b)^3")

    choice = int(input("Choose the correct identity: "))

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    if choice == 1:
        result = a * a + 2 * a * b + b * b
        print("(a + b)^2 =", result)

    elif choice == 2:
        result = a * a - 2 * a * b + b * b
        print("(a - b)^2 =", result)

    elif choice == 3:
        result = a * a - b * b
        print("a^2 - b^2 =", result)

    elif choice == 4:
        result = a * a * a + 3 * a * a * b + 3 * a * b * b + b * b * b
        print("(a + b)^3 =", result)

    elif choice == 5:
        result = a * a * a - 3 * a * a * b + 3 * a * b * b - b * b * b
        print("(a - b)^3 =", result)

    else:
        print("Invalid choice.")

identityselectionchallenge()