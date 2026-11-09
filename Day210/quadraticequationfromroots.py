def quadraticequationfromroots():
    try:
        root1 = float(input("Enter first root: "))
        root2 = float(input("Enter second root: "))

        a = 1
        b = -(root1 + root2)
        c = root1 * root2

        print("\nQuadratic Equation:")
        print(f"x² + ({b})x + ({c}) = 0")

        print("\nCoefficients:")
        print("a =", a)
        print("b =", b)
        print("c =", c)

        print("\nSum of Roots:", root1 + root2)
        print("Product of Roots:", root1 * root2)

    except ValueError:
        print("Please enter valid numeric roots.")

quadraticequationfromroots()