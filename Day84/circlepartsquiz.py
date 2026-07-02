import random

def circleparts():
    questions = [
        ("What is the line from the center to the circle called?", "radius"),
        ("What is the line passing through the center and joining two points on the circle called?", "diameter"),
        ("What is the boundary of a circle called?", "circumference"),
        ("What is the point exactly in the middle of the circle called?", "center"),
        ("What is a line joining any two points on a circle called?", "chord"),
        ("What is a line touching the circle at exactly one point called?", "tangent")
    ]

    score = 0

    random.shuffle(questions)

    for i in range(5):
        print(f"\nQuestion {i+1}")
        print(questions[i][0])

        answer = input("Your Answer: ").lower()

        if answer == questions[i][1]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct Answer:", questions[i][1].capitalize())

    print("\nQuiz Completed")
    print("-" * 25)
    print("Your Score =", score, "/5")

circleparts()