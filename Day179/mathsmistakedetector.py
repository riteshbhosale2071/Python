def mathsmistakedetector():
    print("Maths Mistake Detector :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")

    choice = int(input("Select operation: "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        user_answer = float(input("Enter your answer: "))

        correct_answer = a + b

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        user_answer = float(input("Enter your answer: "))

        correct_answer = a - b

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        user_answer = float(input("Enter your answer: "))

        correct_answer = a * b

    elif choice == 4:
        a = float(input("Enter dividend: "))
        b = float(input("Enter divisor: "))

        if b == 0:
            print("Division by zero is not allowed.")
            return

        user_answer = float(input("Enter your answer: "))
        correct_answer = a / b

    elif choice == 5:
        value = float(input("Enter value: "))
        percentage = float(input("Enter percentage: "))
        user_answer = float(input("Enter your answer: "))

        correct_answer = value * percentage / 100

    else:
        print("Invalid operation.")
        return

    print("\nMistake Analysis :")
    print("Your Answer:", user_answer)
    print("Correct Answer:", round(correct_answer, 2))

    if abs(user_answer - correct_answer) < 0.000001:
        print("Result: Correct")
        print("No mathematical mistake detected.")
    else:
        difference = user_answer - correct_answer

        print("Result: Mistake Detected")
        print("Difference:", round(abs(difference), 2))

        if difference > 0:
            print("Your answer is too high.")
        else:
            print("Your answer is too low.")

mathsmistakedetector()