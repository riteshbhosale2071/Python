import random

def classification():
    score = 0

    for i in range(5):
        angle = random.randint(1, 360)

        print(f"\nQuestion {i+1}")
        print("Classify the angle:", angle, "degrees")

        answer = input("Enter (Acute/Right/Obtuse/Straight/Reflex/Complete): ").lower()

        if angle < 90:
            correct = "acute"
        elif angle == 90:
            correct = "right"
        elif angle < 180:
            correct = "obtuse"
        elif angle == 180:
            correct = "straight"
        elif angle < 360:
            correct = "reflex"
        else:
            correct = "complete"

        if answer == correct:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct Answer:", correct.capitalize())

    print("\nQuiz Completed")
    print("-" * 25)
    print("Your Score =", score, "/5")

classification()