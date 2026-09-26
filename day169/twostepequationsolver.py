def twostepequationsolver():
    print("Two-Step Equation Solver :")
    print("Equation format: ax + b = c")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    for i in range(number_of_equations):
        print("\nEquation", i + 1, ":")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant added to x: "))
        c = float(input("Enter right-hand side value: "))

        print("Equation:", a, "x +", b, "=", c)

        if a == 0:
            if b == c:
                print("Result: Infinitely many solutions.")
            else:
                print("Result: No solution.")
        else:
            step1 = c - b
            solution = step1 / a

            print("Step 1: Subtract", b, "from both sides.")
            print("Equation:", a, "x =", step1)

            print("Step 2: Divide both sides by", a, ".")
            print("Solution: x =", round(solution, 2))

    print("\nEquation Solving Completed.")

twostepequationsolver()