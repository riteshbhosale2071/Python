def equationguessandcheck():
    print("Equation Guess-and-Check Game :")

    number_of_rounds = int(input("Enter the number of rounds: "))

    if number_of_rounds <= 0:
        print("Number of rounds must be greater than zero.")
        return

    score = 0

    for i in range(number_of_rounds):
        print("\nRound", i + 1, "")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant: "))
        c = float(input("Enter right-hand side value: "))

        if a == 0:
            print("Coefficient of x cannot be zero.")
            continue

        correct_solution = (c - b) / a

        print("\nEquation:")
        print(a, "x +", b, "=", c)

        attempts = 3
        solved = False

        for attempt in range(1, attempts + 1):
            guess = float(input("Enter your guess for x: "))

            if round(guess, 2) == round(correct_solution, 2):
                print("Correct! You solved the equation.")
                score += 1
                solved = True
                break

            elif guess < correct_solution:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")

            print("Attempts remaining:", attempts - attempt)

        if not solved:
            print("The correct solution was:", round(correct_solution, 2))

    print("\nGame Result :")
    print("Score:", score, "out of", number_of_rounds)

    if score == number_of_rounds:
        print("Excellent! You solved every equation.")
    elif score >= number_of_rounds / 2:
        print("Good job! Keep practicing.")
    else:
        print("Keep practicing equation solving.")

equationguessandcheck()