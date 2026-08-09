import random

def algebraequationquiz():
    a = random.randint(2, 10)
    x = random.randint(1, 10)
    b = random.randint(1, 20)
    result = a * x + b

    print("Algebra Equation Quiz")
    print(f"Solve: {a}x + {b} = {result}")

    answer = float(input("Enter your answer for x: "))

    if answer == x:
        print("Correct! Well done.")
    else:
        print("Incorrect.")
        print("Correct Answer: x =", x)

algebraequationquiz()