def squareidentity():
    print("Square Identity Generator :")
    print("1. (a + b)^2")
    print("2. (a - b)^2")
    print("3. a^2 - b^2")

    choice = int(input("Enter identity number: "))
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))

    if choice == 1:
        result = a * a + 2 * a * b + b * b
        print("\nIdentity: (a + b)^2")
        print("Expanded Form: a^2 + 2ab + b^2")
        print("Result:", result)

    elif choice == 2:
        result = a * a - 2 * a * b + b * b
        print("\nIdentity: (a - b)^2")
        print("Expanded Form: a^2 - 2ab + b^2")
        print("Result:", result)

    elif choice == 3:
        result = (a + b) * (a - b)
        print("\nIdentity: a^2 - b^2")
        print("Factorised Form: (a + b)(a - b)")
        print("Result:", result)

    else:
        print("Invalid identity number.")

squareidentity()