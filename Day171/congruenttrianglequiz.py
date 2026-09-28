def congruenttrianglequiz():
    print("Congruent Triangle Quiz Generator :")

    number_of_questions = int(input("Enter the number of questions: "))

    if number_of_questions <= 0:
        print("Number of questions must be greater than zero.")
        return

    score = 0

    for i in range(number_of_questions):
        print("\nQuestion", i + 1, ":")

        print("Choose the congruence rule:")
        print("1. SSS")
        print("2. SAS")
        print("3. ASA")
        print("4. RHS")

        choice = int(input("Enter your answer: "))

        side_pairs = int(input("Enter number of equal corresponding side pairs: "))
        angle_pairs = int(input("Enter number of equal corresponding angle pairs: "))
        right_triangles = input("Are both triangles right triangles? (yes/no): ").lower()

        correct_answer = 0

        if side_pairs == 3:
            correct_answer = 1
        elif side_pairs == 2 and angle_pairs >= 1:
            correct_answer = 2
        elif angle_pairs == 2 and side_pairs >= 1:
            correct_answer = 3
        elif right_triangles == "yes" and side_pairs == 2:
            correct_answer = 4

        if correct_answer == 0:
            print("The given evidence is insufficient to establish congruence.")
        else:
            if choice == correct_answer:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")

            if correct_answer == 1:
                print("Correct Rule: SSS")
            elif correct_answer == 2:
                print("Correct Rule: SAS")
            elif correct_answer == 3:
                print("Correct Rule: ASA")
            elif correct_answer == 4:
                print("Correct Rule: RHS")

    print("\nQuiz Result :")
    print("Score:", score, "out of", number_of_questions)

    if score == number_of_questions:
        print("Excellent! All answers are correct.")
    elif score >= number_of_questions / 2:
        print("Good performance!")
    else:
        print("Keep practicing triangle congruence.")

congruenttrianglequiz()