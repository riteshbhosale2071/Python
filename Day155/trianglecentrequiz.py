def trianglecentrequiz():
    print("Triangle Centre Quiz Generator :")

    questions = [
        "Which point is the intersection of the three medians?",
        "Which triangle centre is the intersection of angle bisectors?",
        "Where is the circumcentre of a right triangle located?",
        "Where is the orthocentre of an acute triangle located?",
        "What is the ratio in which the centroid divides a median?",
        "Which four centres coincide in an equilateral triangle?"
    ]

    answers = [
        "Centroid",
        "Incentre",
        "Midpoint of the hypotenuse",
        "Inside the triangle",
        "2:1",
        "Centroid, Incentre, Circumcentre and Orthocentre"
    ]

    score = 0

    for i in range(len(questions)):
        print("\nQuestion", i + 1)
        print(questions[i])

        answer = input("Your answer: ")

        if answer.lower() == answers[i].lower():
            print("Correct!")
            score = score + 1
        else:
            print("Correct answer:", answers[i])

    print("\nQuiz Result :")
    print("Score:", score, "out of", len(questions))

    if score == len(questions):
        print("Excellent!")
    elif score >= 4:
        print("Good job!")
    elif score >= 2:
        print("Keep practicing!")
    else:
        print("Practice triangle centres again.")

trianglecentrequiz()