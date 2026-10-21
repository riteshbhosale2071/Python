def missingproportionterm():
    print("Missing Proportion Term Calculator :")

    print("For a proportion: a : b = c : d")
    print("Choose the term to find:")
    print("1. Find a")
    print("2. Find b")
    print("3. Find c")
    print("4. Find d")

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice.")
            return

        if choice == 1:
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            d = float(input("Enter d: "))

            if d == 0:
                print("Cannot calculate a because d is zero.")
                return

            a = (b * c) / d
            print("Missing term a =", round(a, 6))

        elif choice == 2:
            a = float(input("Enter a: "))
            c = float(input("Enter c: "))
            d = float(input("Enter d: "))

            if c == 0:
                if a == 0 and d == 0:
                    print("The proportion is indeterminate.")
                else:
                    print("No unique value of b can be determined.")
                return

            b = (a * d) / c
            print("Missing term b =", round(b, 6))

        elif choice == 3:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            d = float(input("Enter d: "))

            if b == 0:
                print("Cannot calculate c because b is zero.")
                return

            c = (a * d) / b
            print("Missing term c =", round(c, 6))

        else:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))

            if c == 0:
                if a == 0 and b == 0:
                    print("The proportion is indeterminate.")
                else:
                    print("No unique value of d can be determined.")
                return

            d = (b * c) / a if a != 0 else None

            if d is None:
                print("Cannot calculate d uniquely because a is zero.")
                return

            print("Missing term d =", round(d, 6))

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    print("\nProportion Formula :")
    print("a / b = c / d")
    print("Therefore, a × d = b × c")

missingproportionterm()