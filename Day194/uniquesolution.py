def uniquesolution():
    print("Unique Solution Detector :")
    print("Enter two linear equations in the form ax + by = c.")

    try:
        print("\nFirst Equation:")
        a1 = float(input("Enter coefficient of x: "))
        b1 = float(input("Enter coefficient of y: "))
        c1 = float(input("Enter constant: "))

        print("\nSecond Equation:")
        a2 = float(input("Enter coefficient of x: "))
        b2 = float(input("Enter coefficient of y: "))
        c2 = float(input("Enter constant: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    determinant = a1 * b2 - a2 * b1

    print("\nAnalysis :")
    print("First Equation:", a1, "x +", b1, "y =", c1)
    print("Second Equation:", a2, "x +", b2, "y =", c2)
    print("Determinant:", round(determinant, 6))

    if abs(determinant) > 0.000001:
        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant

        print("\nResult: A unique solution exists.")
        print("Value of x:", round(x, 4))
        print("Value of y:", round(y, 4))

        print("\nVerification :")
        result1 = a1 * x + b1 * y
        result2 = a2 * x + b2 * y

        print("First equation result:", round(result1, 4))
        print("Second equation result:", round(result2, 4))

        if abs(result1 - c1) < 0.000001 and abs(result2 - c2) < 0.000001:
            print("Both equations are satisfied.")
        else:
            print("A small numerical difference may exist.")

    else:
        print("\nResult: No unique solution exists.")

        if abs(a1 * c2 - a2 * c1) < 0.000001 and abs(b1 * c2 - b2 * c1) < 0.000001:
            print("The equations are dependent.")
            print("Infinitely many solutions may exist.")
        else:
            print("The equations are inconsistent.")
            print("No solution exists.")

    print("\nRule :")
    print("A unique solution exists when a1*b2 - a2*b1 is non-zero.")

uniquesolution()