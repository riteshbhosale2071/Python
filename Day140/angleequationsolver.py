def angleequationsolver():
    print("Solve an angle equation of the form: a*x + b = c")

    a = float(input("Enter coefficient of x (a): "))
    b = float(input("Enter constant (b): "))
    c = float(input("Enter right-hand side value (c): "))

    if a == 0:
        if b == c:
            print("Infinite solutions.")
        else:
            print("No solution.")
        return

    x = (c - b) / a

    if x <= 0 or x >= 180:
        print("Solution:", x)
        print("The solution is not a valid angle.")
    else:
        print("Missing Angle:", x, "°")

angleequationsolver()