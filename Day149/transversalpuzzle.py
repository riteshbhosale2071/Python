import random

def transversalpuzzle():
    print("Transversal Puzzle Generator with Missing Angles :")

    number_of_missing = int(input("Enter number of missing angles (1-6): "))

    if number_of_missing < 1 or number_of_missing > 6:
        print("Enter a number between 1 and 6.")
        return

    known_angle = random.randint(20, 160)

    while known_angle == 90:
        known_angle = random.randint(20, 160)

    supplementary_angle = 180 - known_angle

    print("\nGenerated Puzzle :")
    print("Two parallel lines are cut by a transversal.")
    print("One given angle measures:", known_angle, "degrees.")
    print("Find the missing angles.")

    all_angles = [
        known_angle,
        supplementary_angle,
        known_angle,
        supplementary_angle,
        known_angle,
        supplementary_angle,
        known_angle,
        supplementary_angle
    ]

    missing_positions = random.sample(range(8), number_of_missing)

    print("\nAngle Positions:")
    for i in range(8):
        if i in missing_positions:
            print(f"Angle {i + 1}: ?")
        else:
            print(f"Angle {i + 1}: {all_angles[i]}°")

    print("\nSolve the Missing Angles :")

    answers = []

    for position in missing_positions:
        answer = float(input(f"Enter Angle {position + 1}: "))
        answers.append((position + 1, answer, all_angles[position]))

    print("\nPuzzle Results :")

    score = 0

    for position, user_answer, correct_answer in answers:
        if abs(user_answer - correct_answer) < 0.000001:
            print(f"Angle {position}: Correct!")
            score += 1
        else:
            print(
                f"Angle {position}: Incorrect. "
                f"Correct answer = {correct_answer}°"
            )

    print(f"\nScore: {score}/{number_of_missing}")

    if score == number_of_missing:
        print("Excellent! All missing angles are correct.")
    else:
        print("Keep practicing transversal angle relationships.")

transversalpuzzle()