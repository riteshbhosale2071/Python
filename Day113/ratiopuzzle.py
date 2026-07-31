def ratiopuzzle():
    a = int(input("Enter the first number of the ratio: "))
    b = int(input("Enter the second number of the ratio: "))
    multiplier = int(input("Enter the multiplier: "))

    print("\nComplete the ratio:")
    print(f"{a} : {b} = {a * multiplier} : ?")

    answer = int(input("Enter the missing value: "))

    correct = b * multiplier

    if answer == correct:
        print("Correct!")
    else:
        print("Wrong! The correct answer is", correct)

ratiopuzzle()