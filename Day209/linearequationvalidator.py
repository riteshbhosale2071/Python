def linearequationvalidator():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter constant b: "))
        c = float(input("Enter constant c: "))

        print(f"Equation: {a}x + {b} = {c}")

        if a == 0:
            if b == c:
                print("Infinite solutions")
            else:
                print("No solution")
        else:
            x = (c - b) / a
            print("Solution: x =", round(x, 4))

            if abs((a * x + b) - c) < 1e-9:
                print("Equation is valid and verified.")
            else:
                print("Equation verification failed.")

    except ValueError:
        print("Please enter valid numeric values.")

linearequationvalidator()