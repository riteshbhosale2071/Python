import random

def exponentpuzzle():
    print("Exponent Puzzle Generator :")

    puzzle_type = random.randint(1, 5)

    if puzzle_type == 1:
        base = random.randint(2, 5)
        exponent1 = random.randint(2, 5)
        exponent2 = random.randint(2, 4)

        answer = exponent1 + exponent2

        print("\nPuzzle:")
        print(f"{base}^{exponent1} × {base}^{exponent2} = {base}^?")

    elif puzzle_type == 2:
        base = random.randint(2, 5)
        exponent1 = random.randint(4, 8)
        exponent2 = random.randint(1, 3)

        answer = exponent1 - exponent2

        print("\nPuzzle:")
        print(f"{base}^{exponent1} ÷ {base}^{exponent2} = {base}^?")

    elif puzzle_type == 3:
        base = random.randint(2, 5)
        exponent1 = random.randint(2, 4)
        exponent2 = random.randint(2, 4)

        answer = exponent1 * exponent2

        print("\nPuzzle:")
        print(f"({base}^{exponent1})^{exponent2} = {base}^?")

    elif puzzle_type == 4:
        base = random.randint(2, 9)
        exponent = random.randint(2, 5)

        answer = base ** exponent

        print("\nPuzzle:")
        print(f"{base}^{exponent} = ?")

    else:
        base = random.randint(2, 9)
        exponent = random.randint(2, 5)

        answer = exponent

        print("\nPuzzle:")
        print(f"{base}^{exponent} = {base}^?")

    print("\nFind the missing value.")

    user_answer = int(input("Your answer: "))

    if user_answer == answer:
        print("Correct! Well done.")
    else:
        print("Incorrect.")
        print("Correct answer:", answer)

exponentpuzzle()