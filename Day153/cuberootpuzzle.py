import random

def cuberootpuzzle():
    print("Cube Root Puzzle Generator :")

    puzzle_type = random.randint(1, 4)

    if puzzle_type == 1:
        root = random.randint(2, 12)
        number = root ** 3
        answer = root

        print("\nPuzzle:")
        print(f"Find the cube root of {number}.")

    elif puzzle_type == 2:
        root = random.randint(2, 10)
        number = root ** 3
        answer = root

        print("\nPuzzle:")
        print(f"□³ = {number}")
        print("Find the missing number.")

    elif puzzle_type == 3:
        root = random.randint(2, 10)
        number = root ** 3
        multiplier = random.randint(2, 5)
        number *= multiplier ** 3
        answer = root * multiplier

        print("\nPuzzle:")
        print(f"Find the cube root of {number}.")

    else:
        root = random.randint(2, 10)
        cube = root ** 3
        answer = root

        print("\nPuzzle:")
        print(f"Which integer has {cube} as its cube?")

    print("\nEnter your answer:")
    user_answer = int(input("Answer: "))

    print("\nPuzzle Result :")

    if user_answer == answer:
        print("Correct! Well done.")
    else:
        print("Incorrect.")
        print("Correct answer:", answer)

cuberootpuzzle()