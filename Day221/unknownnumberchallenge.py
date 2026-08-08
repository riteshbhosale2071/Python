import random

def unknownnumberchallenge():
    number = random.randint(1, 20)
    operation = random.choice(["+", "-", "*"])
    value = random.randint(1, 10)

    if operation == "+":
        result = number + value
        print(f"Find the unknown number: x + {value} = {result}")
    elif operation == "-":
        result = number - value
        print(f"Find the unknown number: x - {value} = {result}")
    else:
        result = number * value
        print(f"Find the unknown number: x × {value} = {result}")

    answer = int(input("Enter the value of x: "))

    if answer == number:
        print("Correct! Challenge solved.")
    else:
        print("Wrong!")
        print("Correct Answer: x =", number)

unknownnumberchallenge()