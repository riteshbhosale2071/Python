def equationpuzzle():
    print("Equation Puzzle Generator :")

    number_of_puzzles = int(input("Enter the number of puzzles: "))

    if number_of_puzzles <= 0:
        print("Number of puzzles must be greater than zero.")
        return

    score = 0

    for i in range(number_of_puzzles):
        print("\nPuzzle", i + 1, ":")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant: "))
        x = float(input("Enter hidden value of x: "))

        answer = a * x + b

        print("\nSolve the puzzle:")
        print(a, "x +", b, "=", round(answer, 2))

        user_answer = float(input("Enter your answer for x: "))

        if round(user_answer, 2) == round(x, 2):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print("Correct answer: x =", round(x, 2))

    print("\nPuzzle Results :")
    print("Score:", score, "out of", number_of_puzzles)

    if score == number_of_puzzles:
        print("Excellent! All puzzles solved correctly.")
    elif score >= number_of_puzzles / 2:
        print("Good performance!")
    else:
        print("Keep practicing equations.")

equationpuzzle()