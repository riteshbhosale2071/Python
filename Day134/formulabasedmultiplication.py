def formulabasedmultiplication():
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))

    print("Choose a formula:")
    print("1. (a + b)²")
    print("2. (a - b)²")
    print("3. (a + b)(a - b)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        result = a ** 2 + 2 * a * b + b ** 2
        print("(a + b)² =", result)

    elif choice == "2":
        result = a ** 2 - 2 * a * b + b ** 2
        print("(a - b)² =", result)

    elif choice == "3":
        result = a ** 2 - b ** 2
        print("(a + b)(a - b) =", result)

    else:
        print("Invalid choice.")

formulabasedmultiplication()