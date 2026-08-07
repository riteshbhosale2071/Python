def onevariableequation():
    a = float(input("Enter the coefficient of x: "))
    b = float(input("Enter the constant term: "))

    # Equation: ax + b = 0

    if a != 0:
        x = -b / a
        print("Solution: x =", round(x, 2))
    else:
        print("No unique solution exists.")

onevariableequation()