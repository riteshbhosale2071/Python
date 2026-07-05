def error():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    user_answer = int(input("Enter your multiplication answer: "))

    correct_answer = num1 * num2

    print("\nMultiplication Error Report")
    print("-" * 35)
    print("First Number  =", num1)
    print("Second Number =", num2)
    print("Your Answer   =", user_answer)
    print("Correct Answer =", correct_answer)

    if user_answer == correct_answer:
        print("Result: Correct!")
    else:
        print("Result: Incorrect!")
        print("Difference =", abs(correct_answer - user_answer))

error()