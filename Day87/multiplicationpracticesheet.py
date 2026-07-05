import random

def practice():
    n = int(input("Enter the number of questions: "))

    print("\nMultiplication Practice Sheet")
    print("-" * 40)

    score = 0

    for i in range(1, n + 1):
        num1 = random.randint(10, 99)
        num2 = random.randint(2, 9)

        answer = int(input(f"Q{i}. {num1} × {num2} = "))

        correct_answer = num1 * num2

        if answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct Answer =", correct_answer, "\n")

    print("-" * 40)
    print("Practice Completed")
    print("Correct Answers =", score)
    print("Wrong Answers =", n - score)
    print("Score =", score, "/", n)

practice()