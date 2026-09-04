import random

def parallellinepuzzle():
    print("Parallel-Line Puzzle Generator :")

    known_angle = random.randint(20, 160)

    relationships = [
        ("Corresponding Angles", known_angle),
        ("Alternate Interior Angles", known_angle),
        ("Alternate Exterior Angles", known_angle),
        ("Co-Interior Angles", 180 - known_angle),
        ("Vertically Opposite Angles", known_angle),
        ("Linear Pair", 180 - known_angle)
    ]

    relationship, answer = random.choice(relationships)

    print("\nGenerated Puzzle :")
    print("Two parallel lines are cut by a transversal.")
    print("One angle measures", known_angle, "degrees.")
    print("The unknown angle has the relationship:", relationship)
    print("Find the unknown angle.")

    user_answer = float(input("\nEnter your answer: "))

    if user_answer == answer:
        print("Correct! Well done.")
    else:
        print("Incorrect.")
        print("Correct Answer:", answer, "degrees")

parallellinepuzzle()