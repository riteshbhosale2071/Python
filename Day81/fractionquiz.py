import random

def fraction_quiz_game():
    score = 0

    for i in range(5):
        denominator = random.randint(2, 10)

        numerator1 = random.randint(1, denominator - 1)
        numerator2 = random.randint(1, denominator - 1)

        print(f"\nQuestion {i+1}")
        print(f"{numerator1}/{denominator} + {numerator2}/{denominator} = ?")

        answer = int(input("Enter numerator of the answer: "))

        correct = numerator1 + numerator2

        if answer == correct:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct Answer =", correct, "/", denominator)

    print("\nYour Score =", score, "/5")

fraction_quiz_game()