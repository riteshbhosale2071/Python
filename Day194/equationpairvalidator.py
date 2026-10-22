def equationpairvalidator():
    print("Equation Pair Validator :")
    print("Equation format: ax + by = c")

    try:
        n = int(input("Enter the number of equations: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of equations must be greater than zero.")
        return

    equations = []

    for i in range(n):
        print("\nEquation", i + 1)

        try:
            a = float(input("Enter coefficient of x: "))
            b = float(input("Enter coefficient of y: "))
            c = float(input("Enter constant: "))
        except ValueError:
            print("Invalid input! Enter numeric values.")
            return

        equations.append((a, b, c))

    try:
        x = float(input("\nEnter the value of x: "))
        y = float(input("Enter the value of y: "))
    except ValueError:
        print("Invalid input! Enter numeric values for x and y.")
        return

    valid_count = 0
    invalid_count = 0

    print("\nEquation Validation Results :")

    for i, equation in enumerate(equations):
        a, b, c = equation
        left_side = a * x + b * y

        print("\nEquation", i + 1, ":", a, "x +", b, "y =", c)
        print("Calculated Left Side:", round(left_side, 4))
        print("Expected Right Side:", c)

        if abs(left_side - c) < 0.000001:
            print("Status: Valid")
            valid_count += 1
        else:
            print("Status: Invalid")
            print("Difference:", round(abs(left_side - c), 4))
            invalid_count += 1

    print("\nSummary :")
    print("Total Equations:", n)
    print("Valid Equations:", valid_count)
    print("Invalid Equations:", invalid_count)

    if invalid_count == 0:
        print("The given (x, y) pair satisfies all equations.")
    elif valid_count == 0:
        print("The given (x, y) pair satisfies none of the equations.")
    else:
        print("The given (x, y) pair satisfies some equations only.")

equationpairvalidator()