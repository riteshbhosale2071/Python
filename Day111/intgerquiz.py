def integerquiz():
    num1 = 15
    num2 = -8

    print("What is", num1, "+", num2, "?")
    answer = int(input("Enter your answer: "))

    if answer == num1 + num2:
        print("Correct!")
    else:
        print("Wrong! The correct answer is", num1 + num2)

integerquiz()