def equationsolutioncomparison():
    print("Equation Solution Comparison :")
    print("Equations must be in the form: ax + b = c")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    solutions = []

    for i in range(number_of_equations):
        print("\nEquation", i + 1, ":")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant: "))
        c = float(input("Enter right-hand side value: "))

        print("Equation:", a, "x +", b, "=", c)

        if a == 0:
            if b == c:
                print("Result: Infinitely many solutions.")
                solutions.append("Infinite")
            else:
                print("Result: No solution.")
                solutions.append("None")
        else:
            solution = (c - b) / a
            solutions.append(solution)

            print("Solution: x =", round(solution, 2))

    print("\nSolution Comparison :")

    numeric_solutions = []

    for solution in solutions:
        if solution != "Infinite" and solution != "None":
            numeric_solutions.append(solution)

    if len(numeric_solutions) == 0:
        print("No unique numerical solutions to compare.")
        return

    highest = numeric_solutions[0]
    lowest = numeric_solutions[0]

    for solution in numeric_solutions:
        if solution > highest:
            highest = solution

        if solution < lowest:
            lowest = solution

    print("Highest Solution:", round(highest, 2))
    print("Lowest Solution:", round(lowest, 2))
    print("Difference:", round(highest - lowest, 2))

    if highest == lowest:
        print("All numerical solutions are equal.")
    else:
        print("The numerical solutions are different.")

equationsolutioncomparison()