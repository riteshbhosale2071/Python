def algebraicformula():
    print("Choose an algebraic formula:")
    print("1. (a + b)² = a² + 2ab + b²")
    print("2. (a - b)² = a² - 2ab + b²")
    print("3. a² - b² = (a - b)(a + b)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        result = a**2 + 2*a*b + b**2
        print("(a + b)² =", result)

    elif choice == "2":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        result = a**2 - 2*a*b + b**2
        print("(a - b)² =", result)

    elif choice == "3":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        result = (a - b) * (a + b)
        print("a² - b² =", result)

    else:
        print("Invalid choice.")

algebraicformula()