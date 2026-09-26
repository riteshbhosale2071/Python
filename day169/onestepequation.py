def onestepequation():
    print("One-Step Equation Generator :")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    for i in range(number_of_equations):
        print("\nEquation", i + 1, ":")

        operation = input("Enter operation (add, subtract, multiply, divide): ").lower()
        number = float(input("Enter the number: "))
        answer = float(input("Enter the solution value: "))

        if operation == "add":
            print("Generated Equation: x +", number, "=", answer)
            solution = answer - number

        elif operation == "subtract":
            print("Generated Equation: x -", number, "=", answer)
            solution = answer + number

        elif operation == "multiply":
            print("Generated Equation:", number, "x =", answer)

            if number == 0:
                print("Cannot solve because the coefficient is zero.")
                continue

            solution = answer / number

        elif operation == "divide":
            print("Generated Equation: x /", number, "=", answer)

            if number == 0:
                print("Cannot divide by zero.")
                continue

            solution = answer * number

        else:
            print("Invalid operation.")
            continue

        print("Solution: x =", round(solution, 2))

    print("\nEquation Generation Completed.")

onestepequation()