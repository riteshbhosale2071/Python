def integeraddition():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    answer = int(input("Enter the sum of the two integers: "))

    if answer == num1 + num2:
        print("Correct!")
    else:
        print("Wrong! The correct sum is", num1 + num2)

integeraddition()