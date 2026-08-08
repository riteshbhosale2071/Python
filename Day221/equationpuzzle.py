import random

def equationpuzzle():
    a = random.randint(2, 10)
    x = random.randint(1, 10)
    b = random.randint(1, 20)

    result = a * x + b

    print("Equation Puzzle:")
    print(f"{a}x + {b} = {result}")

    answer = float(input("Find the value of x: "))

    if answer == x:
        print("Correct! You solved the puzzle.")
    else:
        print("Incorrect.")
        print("Correct Answer: x =", x)

equationpuzzle()