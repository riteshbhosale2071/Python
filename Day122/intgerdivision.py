def integerdivision():
    num1 = int(input("Enter the dividend: "))
    num2 = int(input("Enter the divisor: "))

    if num2 == 0:
        print("Division by zero is not allowed.")
    elif (num1 >= 0 and num2 > 0) or (num1 < 0 and num2 < 0):
        print("The quotient is Positive.")
    else:
        print("The quotient is Negative.")

integerdivision()