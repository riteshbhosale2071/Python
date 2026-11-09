def quadraticpolynomialclassifier():
    try:
        a = float(input("Enter coefficient of x²: "))
        b = float(input("Enter coefficient of x: "))
        c = float(input("Enter constant term: "))

        if a == 0:
            print("Not a quadratic polynomial.")
            return

        print("\nPolynomial: ax² + bx + c")
        print("Discriminant:", b ** 2 - 4 * a * c)

        if b == 0 and c == 0:
            print("Classification: Pure quadratic polynomial")
        elif b == 0:
            print("Classification: Quadratic polynomial without linear term")
        elif c == 0:
            print("Classification: Quadratic polynomial without constant term")
        else:
            print("Classification: Complete quadratic polynomial")

        if a > 0:
            print("Leading coefficient: Positive")
        else:
            print("Leading coefficient: Negative")

        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            print("Roots: Two distinct real roots")
        elif discriminant == 0:
            print("Roots: Two equal real roots")
        else:
            print("Roots: Two complex roots")

    except ValueError:
        print("Please enter valid numeric coefficients.")

quadraticpolynomialclassifier()