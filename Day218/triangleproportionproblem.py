def triangleproportionproblem():
    print("Triangle Proportion Problem Solver")

    print("\nChoose the proportion to solve:")
    print("1. Find x using a/b = c/x")
    print("2. Find x using a/x = c/d")
    print("3. Find x using a/b = x/d")
    print("4. Find x using a/b = x/c")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        if a == 0 or b == 0:
            print("Division by zero is not allowed.")
            return

        x = (b * c) / a

    elif choice == "2":
        a = float(input("Enter a: "))
        c = float(input("Enter c: "))
        d = float(input("Enter d: "))

        if c == 0:
            print("Division by zero is not allowed.")
            return

        x = (a * d) / c

    elif choice == "3":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        d = float(input("Enter d: "))

        if a == 0:
            print("Division by zero is not allowed.")
            return

        x = (b * d) / a

    elif choice == "4":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        if a == 0:
            print("Division by zero is not allowed.")
            return

        x = (a * c) / b

    else:
        print("Invalid choice.")
        return

    print("\nThe missing value of x =", round(x, 4))

triangleproportionproblem()