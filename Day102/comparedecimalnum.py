def comparedecimals():
    num1 = float(input("Enter first decimal number: "))
    num2 = float(input("Enter second decimal number: "))

    if num1 > num2:
        print(num1, "is greater than", num2)
    elif num1 < num2:
        print(num2, "is greater than", num1)
    else:
        print("Both decimal numbers are equal")

comparedecimals()