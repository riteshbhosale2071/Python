def intmultiplysign():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    if num1 == 0 or num2 == 0:
        print("Result Sign: Zero")
    elif (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
        print("Result Sign: Positive")
    else:
        print("Result Sign: Negative")

intmultiplysign()