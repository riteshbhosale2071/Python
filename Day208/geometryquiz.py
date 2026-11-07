import random

def geometryquiz():
    print("Welcome to Geometry Quiz Application")
    print("Test your Geometry Knowledge!")

    questions = [
        {
            "question": "What is the sum of interior angles of a triangle?",
            "options": ["90 degrees", "180 degrees", "270 degrees", "360 degrees"],
            "answer": 2
        },
        {
            "question": "What is the area of a square with side 5 cm?",
            "options": ["10 cm²", "20 cm²", "25 cm²", "30 cm²"],
            "answer": 3
        },
        {
            "question": "How many sides does a hexagon have?",
            "options": ["5", "6", "7", "8"],
            "answer": 2
        },
        {
            "question": "What is the value of pi approximately?",
            "options": ["2.14", "3.14", "4.14", "5.14"],
            "answer": 2
        },
        {
            "question": "What is the formula for the circumference of a circle?",
            "options": ["πr²", "2πr", "πd²", "4πr²"],
            "answer": 2
        },
        {
            "question": "How many degrees are there in a right angle?",
            "options": ["45 degrees", "60 degrees", "90 degrees", "180 degrees"],
            "answer": 3
        },
        {
            "question": "What is the volume of a cube with side 3 cm?",
            "options": ["9 cm³", "18 cm³", "27 cm³", "36 cm³"],
            "answer": 3
        },
        {
            "question": "Which shape has exactly three sides?",
            "options": ["Square", "Rectangle", "Triangle", "Pentagon"],
            "answer": 3
        },
        {
            "question": "What is the sum of angles in a quadrilateral?",
            "options": ["180 degrees", "270 degrees", "360 degrees", "540 degrees"],
            "answer": 3
        },
        {
            "question": "What is the longest side of a right-angled triangle called?",
            "options": ["Base", "Height", "Hypotenuse", "Median"],
            "answer": 3
        }
    ]

    random.shuffle(questions)

    score = 0

    for i, question in enumerate(questions, start=1):
        print("\nQuestion", i, "of", len(questions))
        print(question["question"])

        for j, option in enumerate(question["options"], start=1):
            print(f"{j}. {option}")

        try:
            answer = int(input("Enter your answer (1-4): "))

            if answer < 1 or answer > 4:
                print("Invalid option. No point awarded.")
                continue

            if answer == question["answer"]:
                print("Correct answer!")
                score += 1
            else:
                correct = question["options"][question["answer"] - 1]
                print("Wrong answer!")
                print("Correct answer:", correct)

        except ValueError:
            print("Please enter a valid option.")

    print("\nQUIZ RESULT :")
    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Incorrect Answers:", len(questions) - score)
    print("Final Score:", str(score) + "/" + str(len(questions)))

    percentage = (score / len(questions)) * 100
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 90:
        print("Excellent! Outstanding performance!")
    elif percentage >= 70:
        print("Great job! Keep practicing.")
    elif percentage >= 50:
        print("Good effort! You can improve.")
    else:
        print("Keep learning and try again!")

geometryquiz()