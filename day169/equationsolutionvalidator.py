def equationsolutionvalidator():
    print("Equation Solution Validator :")
    print("Equation format: ax + b = c")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    for i in range(number_of_equations):
        print("\nEquation", i + 1, ":")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant: "))
        c = float(input("Enter right-hand side value: "))
        proposed_solution = float(input("Enter proposed value of x: "))

        print("\nEquation:")
        print(a, "x +", b, "=", c)

        left_side = a * proposed_solution + b
        right_side = c

        print("\nSubstitute x =", proposed_solution)
        print("Left Side:", round(left_side, 2))
        print("Right Side:", round(right_side, 2))

        if round(left_side, 2) == round(right_side, 2):
            print("Result: The proposed solution is valid.")
        else:
            print("Result: The proposed solution is invalid.")

            if a != 0:
                correct_solution = (c - b) / a
                print("Correct solution: x =", round(correct_solution, 2))
            else:
                if b == c:
                    print("The equation has infinitely many solutions.")
                else:
                    print("The equation has no solution.")

    print("\nSolution Validation Completed.")

equationsolutionvalidator()