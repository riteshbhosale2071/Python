def simultaneousequation():
    print("Simultaneous Equation :")

    print("\nEquation Format:")
    print("a1x + b1y = c1")
    print("a2x + b2y = c2")

    print("\nEnter coefficients of first equation:")
    a1 = float(input("Enter a1: "))
    b1 = float(input("Enter b1: "))
    c1 = float(input("Enter c1: "))

    print("\nEnter coefficients of second equation:")
    a2 = float(input("Enter a2: "))
    b2 = float(input("Enter b2: "))
    c2 = float(input("Enter c2: "))

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
            print("\nThe equations have infinitely many solutions.")
        else:
            print("\nThe equations have no solution.")
        return

    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    print("\nSolution:")
    print(f"x = {x:.2f}")
    print(f"y = {y:.2f}")

    print("\nVerification:")
    print(f"First Equation LHS: {a1 * x + b1 * y:.2f}")
    print(f"First Equation RHS: {c1:.2f}")
    print(f"Second Equation LHS: {a2 * x + b2 * y:.2f}")
    print(f"Second Equation RHS: {c2:.2f}")

simultaneousequation()