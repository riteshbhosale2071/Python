import random

def equationmatching():
    x = random.randint(1, 10)
    a = random.randint(2, 10)
    b = random.randint(1, 20)

    result = a * x + b

    print("Equation Matching Game")
    print(f"Equation: {a}x + {b} = {result}")
    print("\nChoose the matching value of x:")
    print("1.", x)
    print("2.", x + 1)
    print("3.", x + 2)
    print("4.", max(1, x - 1))

    answer = int(input("Enter your choice (1-4): "))

    if answer == 1:
        print("Correct! You found the matching solution.")
    else:
        print("Incorrect.")
        print("Correct Answer: Option 1, x =", x)

equationmatching()