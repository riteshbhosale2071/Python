def quiz():
    score = 0

    for i in range(5):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        answer = int(input(f"{num1} × {num2} = "))

        if answer == num1 * num2:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("Final Score =", score)

quiz()