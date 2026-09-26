def missingconstantfinder():
    print("Missing Constant Finder :")
    print("Equation format: ax + b = c")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    for i in range(number_of_equations):
        print("\nEquation", i + 1, ":")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter known constant b (enter 0 if missing): "))
        c = float(input("Enter right-hand side constant c: "))
        x = float(input("Enter value of x: "))

        print("\nEquation:")
        print(a, "x + b =", c)

        missing_constant = c - (a * x)

        print("\nSubstitute x =", x)
        print(a, "*", x, "+ b =", c)

        if b == 0:
            print("Missing constant b:", round(missing_constant, 2))
        else:
            if round(b, 2) == round(missing_constant, 2):
                print("The given constant is correct.")
                print("Constant b:", round(b, 2))
            else:
                print("The given constant is incorrect.")
                print("Correct missing constant b:", round(missing_constant, 2))

    print("\nMissing Constant Analysis Completed.")

missingconstantfinder()