import random

def luckynum():
    lucky = random.randint(1, 10)

    guess = int(input("Guess the lucky number (1-10): "))

    if guess == lucky:
        print("Congratulations! You guessed correctly.")

    else:
        print("Lucky Number was", lucky)

luckynum()