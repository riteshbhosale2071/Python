import random

def equationgenerator():
    a = random.randint(1, 10)
    x = random.randint(1, 10)
    b = random.randint(1, 20)

    result = a * x + b

    print("Solve the following equation:")
    print(f"{a}x + {b} = {result}")

    answer = float(input("Enter the value of x: "))

    if answer == x:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer: x =", x)

equationgenerator()