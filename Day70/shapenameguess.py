def guess():
    answer = "triangle"

    guess = input("I have 3 sides. Guess the shape: ").lower()

    if guess == answer:
        print("Correct!")

    else:
        print("Wrong! The answer is Triangle.")

guess()