def equationverification():
    a = float(input("Enter the coefficient of x: "))
    x = float(input("Enter the value of x: "))
    b = float(input("Enter the constant term: "))
    result = float(input("Enter the right side of the equation: "))

    left_side = a * x + b

    if left_side == result:
        print("The equation is verified.")
    else:
        print("The equation is not verified.")
        print("Left Side:", left_side)
        print("Right Side:", result)

equationverification()