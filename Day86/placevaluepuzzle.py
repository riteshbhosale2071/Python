import random

def puzzle():
    number = random.randint(10000, 99999)

    places = ["Ten-Thousands", "Thousands", "Hundreds", "Tens", "Ones"]

    position = random.randint(0, 4)

    digit = str(number)[position]

    print("Place Value Puzzle")
    print("-" * 30)
    print("Number :", number)
    print("Question: What is the place value of digit", digit, "?")

    answer = int(input("Enter your answer: "))

    place_value = int(digit) * (10 ** (4 - position))

    if answer == place_value:
        print("Correct Answer!")
    else:
        print("Wrong Answer!")
        print("Correct Place Value =", place_value)

puzzle()