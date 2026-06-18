import random

def generate():
    questions = int(input("Enter number of questions: "))

    print("\nAddition Worksheet")
    print("-" * 20)

    for i in range(1, questions + 1):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)

        print(f"{i}. {num1} + {num2} = _____")

generate()