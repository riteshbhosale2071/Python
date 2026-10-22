def simultaneousequation():
    print("Simultaneous Equation :")
    print("Equation format: ax + by = c")
    print("Solve two equations with two variables.")

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
    determinant_x = c1 * b2 - c2 * b1
    determinant_y = a1 * c2 - a2 * c1

    print("\nCalculation :")
    print("Determinant:", round(determinant, 4))

    if abs(determinant) > 0.000001:
        x = determinant_x / determinant
        y = determinant_y / determinant

        print("\nSolution :")
        print("x =", round(x, 4))
        print("y =", round(y, 4))

        print("\nVerification :")
        result1 = a1 * x + b1 * y
        result2 = a2 * x + b2 * y

        print("First equation left side:", round(result1, 4))
        print("First equation right side:", c1)
        print("Second equation left side:", round(result2, 4))
        print("Second equation right side:", c2)

        if abs(result1 - c1) < 0.000001 and abs(result2 - c2) < 0.000001:
            print("Verification successful!")
        else:
            print("A small rounding difference may exist.")

    else:
        if abs(determinant_x) < 0.000001 and abs(determinant_y) < 0.000001:
            print("Infinitely many solutions exist.")
            print("Both equations represent the same line.")
        else:
            print("No solution exists.")
            print("The equations represent parallel distinct lines.")

    print("\nEquation Summary :")
    print("Equation 1:", a1, "x +", b1, "y =", c1)
    print("Equation 2:", a2, "x +", b2, "y =", c2)

simultaneousequation()