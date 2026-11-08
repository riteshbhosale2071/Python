def equationsolutionverifier():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter constant c: "))
        x = float(input("Enter proposed value of x: "))

        left_side = a * x + b

        print("\nEquation: ax + b = c")
        print("Left Hand Side:", left_side)
        print("Right Hand Side:", c)

        if abs(left_side - c) < 1e-9:
            print("Result: Correct solution")
            print("The given value satisfies the equation.")
        else:
            print("Result: Incorrect solution")
            print("The given value does not satisfy the equation.")

    except ValueError:
        print("Please enter valid numeric values.")

equationsolutionverifier()