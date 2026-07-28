def integercomparison():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    if num1 > num2:
        print(num1, "is greater than", num2)
    elif num1 < num2:
        print(num2, "is greater than", num1)
    else:
        print("Both integers are equal")

integercomparison()