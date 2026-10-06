def adaptivemathsquiz():
    print("Adaptive Maths Quiz :")

    score = 0
    difficulty = 1

    for question_number in range(1, 6):
        print("\nQuestion", question_number)

        if difficulty == 1:
            a = question_number * 5
            b = question_number * 3

            print("What is", a, "+", b, "?")
            answer = float(input("Enter your answer: "))
            correct_answer = a + b

        elif difficulty == 2:
            a = question_number * 8
            b = question_number * 4

            print("What is", a, "×", b, "?")
            answer = float(input("Enter your answer: "))
            correct_answer = a * b

        else:
            a = question_number * 10
            b = question_number * 2
            c = question_number * 3

            print("Solve:", a, "x +", b, "=", c * 10)
            answer = float(input("Enter the value of x: "))
            correct_answer = ((c * 10) - b) / a

        if abs(answer - correct_answer) < 0.000001:
            print("Correct!")
            score += 1

            if difficulty < 3:
                difficulty += 1

            print("Difficulty increased.")
        else:
            print("Incorrect.")
            print("Correct answer:", round(correct_answer, 2))

            if difficulty > 1:
                difficulty -= 1

            print("Difficulty decreased.")

    print("\nQuiz Result :")
    print("Score:", score, "out of 5")

    if difficulty == 3:
        print("Final Level: Hard")
    elif difficulty == 2:
        print("Final Level: Medium")
    else:
        print("Final Level: Easy")

adaptivemathsquiz()