import random

def guess():
    secret = random.randint(1, 10)

    guess = int(input("Guess a number (1-10): "))

    if guess == secret:
        print("Correct Guess!")

    else:
        print("Wrong Guess")
        print("Number was", secret)

guess()