def equationvaluecalculator():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        x = float(input("Enter value of x: "))

        result = a * x ** 2 + b * x + c

        print("\nEquation: ax² + bx + c")
        print("Substituted Equation:", a, "*", x, "² +", b, "*", x, "+", c)
        print("Calculated Value:", round(result, 4))

    except ValueError:
        print("Please enter valid numeric values.")

equationvaluecalculator()