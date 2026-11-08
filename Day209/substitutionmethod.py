def substitutionmethod():
    try:
        print("First equation: a1x + b1y = c1")
        a1 = float(input("Enter a1: "))
        b1 = float(input("Enter b1: "))
        c1 = float(input("Enter c1: "))

        print("\nSecond equation: a2x + b2y = c2")
        a2 = float(input("Enter a2: "))
        b2 = float(input("Enter b2: "))
        c2 = float(input("Enter c2: "))

        if a1 == 0 and b1 == 0:
            print("Invalid first equation.")
            return

        if a2 == 0 and b2 == 0:
            print("Invalid second equation.")
            return

        if a1 != 0:
            y_coefficient = b1 - (a1 * b2 / a2) if a2 != 0 else 0

            if a2 != 0:
                x = (c2 - b2 * (c1 / a1)) / (a2 - b2 * b1 / a1)

                if abs(a2 - b2 * b1 / a1) < 1e-9:
                    raise ZeroDivisionError

                y = (c1 - a1 * x) / b1 if b1 != 0 else c2 / b2

            else:
                x = c1 / a1
                y = (c2 - a2 * x) / b2

        else:
            y = c1 / b1
            x = (c2 - b2 * y) / a2

        if (
            abs(a1 * x + b1 * y - c1) < 1e-9
            and abs(a2 * x + b2 * y - c2) < 1e-9
        ):
            print("\nSolution:")
            print("x =", round(x, 4))
            print("y =", round(y, 4))
            print("Both equations are satisfied.")
        else:
            print("No unique solution exists.")

    except ValueError:
        print("Please enter valid numeric values.")
    except ZeroDivisionError:
        print("No unique solution exists.")

substitutionmethod()