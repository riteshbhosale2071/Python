def missingvariable():
    a = float(input("Enter the coefficient of x: "))
    b = float(input("Enter the result of the equation: "))

    # Equation: a × x = b

    if a != 0:
        x = b / a
        print("The missing value of x is:", round(x, 2))
    else:
        print("Cannot find x because the coefficient is 0.")

missingvariable()