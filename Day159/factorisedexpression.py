def factorisedexpression():
    print("Factorised Expression Evaluator :")
    print("1. (a + b)(a - b)")
    print("2. (a + b)^2")
    print("3. (a - b)^2")
    print("4. (a + b)(c + d)")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        result = (a + b) * (a - b)
        print("Result =", result)

    elif choice == 2:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        result = (a + b) * (a + b)
        print("Result =", result)

    elif choice == 3:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        result = (a - b) * (a - b)
        print("Result =", result)

    elif choice == 4:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
        d = int(input("Enter d: "))
        result = (a + b) * (c + d)
        print("Result =", result)

    else:
        print("Invalid choice.")

factorisedexpression()