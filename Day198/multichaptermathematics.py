import random

def multichaptermathematics():
    print("MULTI-CHAPTER MATHEMATICS CHALLENGE GAME :")

    chapters = {
        "Arithmetic": [
            ("What is 25 + 37?", ["52", "62", "72", "60"], "B"),
            ("What is 12 * 8?", ["86", "94", "96", "108"], "C"),
            ("What is 144 / 12?", ["10", "11", "12", "14"], "C"),
            ("What is 15 squared?", ["125", "200", "225", "250"], "C"),
            ("What is 20% of 150?", ["20", "25", "30", "35"], "C")
        ],
        "Algebra": [
            ("Solve: x + 7 = 15.", ["6", "7", "8", "9"], "C"),
            ("Solve: 3x = 21.", ["5", "6", "7", "8"], "C"),
            ("Solve: 2x + 4 = 14.", ["4", "5", "6", "7"], "B"),
            ("Simplify: 4x + 3x.", ["7", "7x", "12x", "x"], "B"),
            ("If x = 3, find x squared + 2.", ["9", "10", "11", "12"], "C")
        ],
        "Geometry": [
            ("How many degrees are in a triangle?", ["90", "180", "270", "360"], "B"),
            ("Find the area of a rectangle of length 8 and width 5.", ["13", "26", "40", "80"], "C"),
            ("How many sides does a hexagon have?", ["5", "6", "7", "8"], "B"),
            ("Find the perimeter of a square with side 6.", ["12", "18", "24", "36"], "C"),
            ("What is the diameter of a circle with radius 7?", ["7", "14", "21", "49"], "B")
        ],
        "Statistics": [
            ("Find the mean of 2, 4, 6.", ["3", "4", "5", "6"], "B"),
            ("Find the median of 1, 3, 5, 7, 9.", ["3", "4", "5", "7"], "C"),
            ("Find the mode of 2, 3, 3, 4, 5.", ["2", "3", "4", "5"], "B"),
            ("Find the range of 10, 15, 20, 25.", ["10", "15", "20", "25"], "B"),
            ("What is the probability of heads on a fair coin toss?", ["0", "1/4", "1/2", "1"], "C")
        ],
        "Number Theory": [
            ("Which is a prime number?", ["9", "15", "17", "21"], "C"),
            ("What is the HCF of 12 and 18?", ["3", "6", "9", "12"], "B"),
            ("What is the LCM of 4 and 6?", ["8", "10", "12", "24"], "C"),
            ("Which number is divisible by 3?", ["124", "125", "126", "127"], "C"),
            ("What is the square root of 169?", ["11", "12", "13", "14"], "C")
        ]
    }

    chapter_names = list(chapters.keys())

    print("\nAvailable Chapters:")
    for index, chapter in enumerate(chapter_names, 1):
        print(str(index) + ".", chapter)

    print(str(len(chapter_names) + 1) + ". All Chapters")

    choice = input("\nSelect a chapter or all chapters: ").strip()

    if choice.isdigit():
        selected_number = int(choice)

        if 1 <= selected_number <= len(chapter_names):
            selected_chapters = [chapter_names[selected_number - 1]]
        elif selected_number == len(chapter_names) + 1:
            selected_chapters = chapter_names[:]
        else:
            print("Invalid chapter selection.")
            return
    else:
        print("Please enter a valid chapter number.")
        return

    try:
        questions_per_chapter = int(
            input("Enter questions per chapter (1-5): ")
        )
    except ValueError:
        print("Please enter a valid integer.")
        return

    if not 1 <= questions_per_chapter <= 5:
        print("Choose between 1 and 5 questions per chapter.")
        return

    random.shuffle(selected_chapters)

    total_questions = 0
    total_score = 0
    chapter_results = []
    wrong_answers = []

    for chapter in selected_chapters:
        print("\n" + "=" * 55)
        print("CHAPTER:", chapter.upper())
        print("=" * 55)

        available_questions = chapters[chapter][:]
        random.shuffle(available_questions)
        selected_questions = available_questions[:questions_per_chapter]

        chapter_score = 0

        for question, options, answer in selected_questions:
            print("\n" + question)

            for index, option in enumerate(options):
                print(chr(65 + index) + ".", option)

            user_answer = input("Your answer (A/B/C/D): ").strip().upper()

            while user_answer not in ["A", "B", "C", "D"]:
                print("Invalid answer. Enter A, B, C, or D.")
                user_answer = input("Your answer: ").strip().upper()

            total_questions += 1

            if user_answer == answer:
                print("Correct! +10 points")
                chapter_score += 10
                total_score += 10
            else:
                correct_option = options[ord(answer) - 65]
                print("Incorrect. Correct answer:", answer + ".", correct_option)
                wrong_answers.append(
                    (chapter, question, answer, correct_option)
                )

        chapter_results.append(
            (chapter, chapter_score, len(selected_questions) * 10)
        )

        print("\nChapter Score:", chapter_score, "/",
              len(selected_questions) * 10)

    maximum_score = total_questions * 10
    percentage = total_score / maximum_score * 100

    print("FINAL GAME RESULTS :")

    print("Chapters Played:", len(selected_chapters))
    print("Questions Attempted:", total_questions)
    print("Total Score:", total_score, "/", maximum_score)
    print("Accuracy:", round(percentage, 2), "%")

    print("\nChapter-Wise Results :")

    for chapter, score, maximum in chapter_results:
        chapter_percentage = score / maximum * 100
        print(
            chapter + ":",
            score, "/", maximum,
            "(" + str(round(chapter_percentage, 2)) + "%)"
        )

    print("\nPerformance Level :")

    if percentage >= 90:
        print("Mathematics Champion! Outstanding performance!")
    elif percentage >= 75:
        print("Excellent work! You have strong mathematical skills.")
    elif percentage >= 50:
        print("Good effort! Continue practicing to improve.")
    else:
        print("Keep learning! Review the chapters and try again.")

    if wrong_answers:
        print("\nReview Incorrect Answers :")

        for chapter, question, answer, correct_option in wrong_answers:
            print("\nChapter:", chapter)
            print(question)
            print("Correct Answer:", answer, "-", correct_option)
    else:
        print("\nPerfect performance! All answers are correct.")

    print("\nThanks for playing the Mathematics Challenge Game!")

multichaptermathematics()