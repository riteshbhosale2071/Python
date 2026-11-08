def simultaneousequation():
    try:
        print("First equation: a1x + b1y = c1")
        a1 = float(input("Enter a1: "))
        b1 = float(input("Enter b1: "))
        c1 = float(input("Enter c1: "))

        print("\nSecond equation: a2x + b2y = c2")
        a2 = float(input("Enter a2: "))
        b2 = float(input("Enter b2: "))
        c2 = float(input("Enter c2: "))

        determinant = a1 * b2 - a2 * b1

        if determinant != 0:
            x = (c1 * b2 - c2 * b1) / determinant
            y = (a1 * c2 - a2 * c1) / determinant

            print("\nSolution:")
            print("x =", round(x, 4))
            print("y =", round(y, 4))

        elif a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
            print("Infinite solutions exist.")

        else:
            print("No solution exists.")

    except ValueError:
        print("Please enter valid numeric values.")

simultaneousequation()