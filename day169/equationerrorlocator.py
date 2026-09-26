def equationerrorlocator():
    print("Equation Error Locator :")
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
        proposed_solution = float(input("Enter proposed solution for x: "))

        print("\nOriginal Equation:")
        print(a, "x +", b, "=", c)

        left_side = a * proposed_solution + b
        error = left_side - c

        print("\nChecking x =", proposed_solution)
        print("Calculated Left Side:", round(left_side, 2))
        print("Expected Right Side:", round(c, 2))
        print("Error:", round(error, 2))

        if abs(error) < 0.000001:
            print("Result: No error found. The solution is correct.")
        else:
            print("Result: Error detected.")

            if left_side > c:
                print("Error Location: Left side is greater than the right side.")
            else:
                print("Error Location: Left side is less than the right side.")

            if a == 0:
                if b == c:
                    print("Equation Status: Infinitely many solutions.")
                else:
                    print("Equation Status: No solution.")
            else:
                correct_solution = (c - b) / a
                print("Correct Solution: x =", round(correct_solution, 2))

                corrected_left_side = a * correct_solution + b
                print("Corrected Left Side:", round(corrected_left_side, 2))

    print("\nEquation Error Analysis Completed.")

equationerrorlocator()