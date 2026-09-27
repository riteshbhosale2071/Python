def equationdifficulty():
    print("Equation Difficulty Generator :")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    for i in range(number_of_equations):
        print("\nEquation", i + 1, ":")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant: "))
        c = float(input("Enter right-hand side value: "))

        print("\nEquation:", a, "x +", b, "=", c)

        if a == 0:
            print("Difficulty: Invalid for a linear equation.")
            continue

        solution = (c - b) / a

        difficulty_score = 0

        if abs(a) > 10:
            difficulty_score += 2
        elif abs(a) > 5:
            difficulty_score += 1

        if abs(b) > 10:
            difficulty_score += 2
        elif abs(b) > 5:
            difficulty_score += 1

        if abs(c) > 10:
            difficulty_score += 2
        elif abs(c) > 5:
            difficulty_score += 1

        if solution < 0:
            difficulty_score += 1

        if difficulty_score <= 2:
            difficulty = "Easy"
        elif difficulty_score <= 5:
            difficulty = "Medium"
        else:
            difficulty = "Hard"

        print("Solution:", round(solution, 2))
        print("Difficulty Score:", difficulty_score)
        print("Difficulty Level:", difficulty)

    print("\nDifficulty Generation Completed.")

equationdifficulty()