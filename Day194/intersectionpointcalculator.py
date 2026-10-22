def intersectionpointcalculator():
    print("Intersection Point Calculator :")
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

    if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
        print("Invalid equation: At least one variable coefficient must be non-zero.")
        return

    determinant = a1 * b2 - a2 * b1

    print("\nIntersection Analysis :")
    print("Equation 1:", a1, "x +", b1, "y =", c1)
    print("Equation 2:", a2, "x +", b2, "y =", c2)

    if abs(determinant) > 0.000001:
        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant

        print("\nThe lines intersect at exactly one point.")
        print("Intersection Point: (", round(x, 4), ",", round(y, 4), ")")

        print("\nVerification :")
        result1 = a1 * x + b1 * y
        result2 = a2 * x + b2 * y

        print("Equation 1 result:", round(result1, 4))
        print("Expected value:", c1)
        print("Equation 2 result:", round(result2, 4))
        print("Expected value:", c2)

    else:
        determinant_x = c1 * b2 - c2 * b1
        determinant_y = a1 * c2 - a2 * c1

        if abs(determinant_x) < 0.000001 and abs(determinant_y) < 0.000001:
            print("\nThe lines overlap completely.")
            print("There are infinitely many intersection points.")
        else:
            print("\nThe lines are parallel.")
            print("There is no intersection point.")

    print("\nCalculation Summary :")
    print("Determinant:", round(determinant, 4))

    if abs(determinant) > 0.000001:
        print("Intersection type: Unique point")
    elif abs(c1 * b2 - c2 * b1) < 0.000001 and abs(a1 * c2 - a2 * c1) < 0.000001:
        print("Intersection type: Coincident lines")
    else:
        print("Intersection type: Parallel lines")

intersectionpointcalculator()