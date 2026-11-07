import random


def geometryexaminationanalyzer():
    print("Geometry Examination Analyzer")

    questions = [
        {
            "question": "What is the sum of angles in a triangle?",
            "options": ["90", "180", "270", "360"],
            "answer": "2"
        },
        {
            "question": "What is the area of a rectangle?",
            "options": ["Length × Width", "2 × Length", "Length + Width", "Length × Height"],
            "answer": "1"
        },
        {
            "question": "How many sides does a hexagon have?",
            "options": ["5", "6", "7", "8"],
            "answer": "2"
        },
        {
            "question": "What is the value of pi approximately?",
            "options": ["2.14", "3.14", "4.14", "5.14"],
            "answer": "2"
        },
        {
            "question": "What is the area of a circle?",
            "options": ["2πr", "πr²", "πd", "r²"],
            "answer": "2"
        },
        {
            "question": "How many degrees are in a right angle?",
            "options": ["45", "60", "90", "180"],
            "answer": "3"
        },
        {
            "question": "What is the volume of a cube?",
            "options": ["Side²", "4 × Side", "Side³", "6 × Side²"],
            "answer": "3"
        },
        {
            "question": "How many diagonals does a rectangle have?",
            "options": ["1", "2", "3", "4"],
            "answer": "2"
        },
        {
            "question": "What is the perimeter of a square?",
            "options": ["Side²", "2 × Side", "3 × Side", "4 × Side"],
            "answer": "4"
        },
        {
            "question": "Which solid has two circular bases?",
            "options": ["Cone", "Sphere", "Cylinder", "Pyramid"],
            "answer": "3"
        }
    ]

    random.shuffle(questions)

    score = 0
    correct_answers = 0
    wrong_answers = 0

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {question['question']}")

        for option_number, option in enumerate(question["options"], start=1):
            print(f"{option_number}. {option}")

        answer = input("Enter your answer (1-4): ").strip()

        if answer not in ["1", "2", "3", "4"]:
            print("Invalid answer. Question marked as incorrect.")
            wrong_answers += 1
        elif answer == question["answer"]:
            print("Correct answer!")
            score += 1
            correct_answers += 1
        else:
            print("Incorrect answer.")
            wrong_answers += 1

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\nExamination Analysis")
    print("Total Questions:", total_questions)
    print("Correct Answers:", correct_answers)
    print("Wrong Answers:", wrong_answers)
    print("Final Score:", score, "/", total_questions)
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        print("Performance: Excellent")
    elif percentage >= 60:
        print("Performance: Good")
    elif percentage >= 40:
        print("Performance: Average")
    else:
        print("Performance: Needs Improvement")

geometryexaminationanalyzer()