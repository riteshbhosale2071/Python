import random
def quiz():
    start = random.randint(1, 10)
    difference = random.randint(2, 5)

    pattern = []

    for i in range(5):
        pattern.append(start + i * difference)

    print("Identify the Pattern:")
    print(pattern)

    answer = int(input("Enter the next number: "))

    correct = pattern[-1] + difference

    if answer == correct:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer =", correct)

quiz()