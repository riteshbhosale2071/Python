def equationconstraintchecker():
    print("Equation Constraint Checker :")
    print("Equation format: ax + b = c")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    for i in range(number_of_equations):
        print("\nEquation", i + 1, "")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant: "))
        c = float(input("Enter right-hand side value: "))

        print("Equation:", a, "x +", b, "=", c)

        if a == 0:
            if b == c:
                print("Equation Status: Identity")
                print("Solution: All real numbers satisfy the equation.")
            else:
                print("Equation Status: Contradiction")
                print("Solution: No solution.")
            continue

        solution = (c - b) / a

        print("Solution: x =", round(solution, 2))

        print("\nChoose a constraint:")
        print("1. x > limit")
        print("2. x < limit")
        print("3. x >= limit")
        print("4. x <= limit")
        print("5. x = limit")

        choice = int(input("Enter constraint choice: "))
        limit = float(input("Enter constraint limit: "))

        valid = False

        if choice == 1:
            if solution > limit:
                valid = True
            print("Constraint: x >", limit)

        elif choice == 2:
            if solution < limit:
                valid = True
            print("Constraint: x <", limit)

        elif choice == 3:
            if solution >= limit:
                valid = True
            print("Constraint: x >=", limit)

        elif choice == 4:
            if solution <= limit:
                valid = True
            print("Constraint: x <=", limit)

        elif choice == 5:
            if solution == limit:
                valid = True
            print("Constraint: x =", limit)

        else:
            print("Invalid constraint choice.")
            continue

        if valid:
            print("Result: The equation solution satisfies the constraint.")
        else:
            print("Result: The equation solution does not satisfy the constraint.")

    print("\nConstraint Checking Completed.")

equationconstraintchecker()