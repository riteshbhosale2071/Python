def equationoperationtracker():
    print("Equation Operation Tracker :")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    for i in range(number_of_equations):
        print("\nEquation", i + 1, ":")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant: "))
        c = float(input("Enter right-hand side value: "))

        print("\nOriginal Equation:")
        print(a, "x +", b, "=", c)

        if a == 0:
            if b == c:
                print("Result: Infinitely many solutions.")
            else:
                print("Result: No solution.")
            continue

        print("\nOperation 1: Subtract", b, "from both sides.")
        first_result = c - b
        print(a, "x =", first_result)

        print("\nOperation 2: Divide both sides by", a)
        solution = first_result / a
        print("x =", round(solution, 2))

        print("\nOperation Summary :")
        print("Original:", a, "x +", b, "=", c)
        print("After subtraction:", a, "x =", first_result)
        print("Final solution: x =", round(solution, 2))

        verification = a * solution + b

        print("\nVerification:")
        print(a, "*", round(solution, 2), "+", b, "=", round(verification, 2))

        if round(verification, 2) == round(c, 2):
            print("Equation verified successfully.")
        else:
            print("Equation verification failed.")

    print("\nOperation Tracking Completed.")

equationoperationtracker()