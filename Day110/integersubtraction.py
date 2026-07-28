def integersubtraction():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    answer = int(input("Enter the result of subtraction: "))

    if answer == num1 - num2:
        print("Correct!")
    else:
        print("Wrong! The correct answer is", num1 - num2)

integersubtraction()