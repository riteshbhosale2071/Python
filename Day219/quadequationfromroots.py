def quadequationfromroots():
    print("Quadratic Equation from Roots")

    root1 = float(input("Enter first root: "))
    root2 = float(input("Enter second root: "))

    a = float(input("Enter coefficient of x² (a): "))

    if a == 0:
        print("Coefficient a cannot be zero.")
        return

    b = -a * (root1 + root2)
    c = a * root1 * root2

    print("\nSum of Roots =", root1 + root2)
    print("Product of Roots =", root1 * root2)

    print("\nGenerated Quadratic Equation:")
    print(f"{a}x² + ({b})x + ({c}) = 0")

    print("\nSimplified Equation:")
    print(f"x² + ({b/a})x + ({c/a}) = 0")

quadequationfromroots()