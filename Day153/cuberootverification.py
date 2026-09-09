import random

def cuberootverification():
    print("Cube Root Verification Game :")

    score = 0
    rounds = int(input("Enter number of rounds: "))

    if rounds <= 0:
        print("Number of rounds must be positive.")
        return

    for round_number in range(1, rounds + 1):
        root = random.randint(2, 12)
        number = root ** 3

        print(f"\nRound {round_number} :")
        print(f"What is the cube root of {number}?")

        user_answer = int(input("Your answer: "))

        if user_answer == root:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print("Correct answer:", root)

        print(f"Verification: {root}³ = {root ** 3}")

    print("\nGame Over :")
    print("Final Score:", score, "/", rounds)

    if score == rounds:
        print("Perfect score! Excellent work.")
    elif score >= rounds / 2:
        print("Good job! Keep practicing.")
    else:
        print("Keep practicing cube roots.")

cuberootverification()