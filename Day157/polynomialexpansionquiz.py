def polynomialexpansionquiz():
    print("Polynomial Expansion Quiz Generator :")

    questions = [
        ("What is the expansion of (x + 2)^2?",
         "x^2 + 4x + 4",
         "x^2 + 2x + 4",
         "x^2 + 4x + 2",
         "x^2 + 4"),

        ("What is the expansion of (x + 3)^2?",
         "x^2 + 6x + 9",
         "x^2 + 3x + 9",
         "x^2 + 9x + 6",
         "x^2 + 6x + 3"),

        ("What is the expansion of (x - 2)^2?",
         "x^2 - 4x + 4",
         "x^2 - 2x + 4",
         "x^2 + 4x + 4",
         "x^2 - 4x - 4"),

        ("What is the expansion of (x + 1)^3?",
         "x^3 + 3x^2 + 3x + 1",
         "x^3 + x^2 + x + 1",
         "x^3 + 2x^2 + 2x + 1",
         "x^3 + 3x + 1"),

        ("What is the coefficient of x in (x + 5)^2?",
         "10",
         "5",
         "25",
         "15")
    ]

    score = 0

    for i in range(len(questions)):
        print("\nQuestion", i + 1)
        print(questions[i][0])

        print("A.", questions[i][1])
        print("B.", questions[i][2])
        print("C.", questions[i][3])
        print("D.", questions[i][4])

        answer = input("Enter A, B, C or D: ").upper()

        if answer == "A":
            print("Correct!")
            score = score + 1
        else:
            print("Correct answer: A")

    print("\nQuiz Result :")
    print("Score:", score, "out of", len(questions))

    if score == len(questions):
        print("Excellent!")
    elif score >= 3:
        print("Good job!")
    else:
        print("Keep practicing polynomial expansions.")

polynomialexpansionquiz()