def missingoperation():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = int(input("Enter result: "))

    if num1 + num2 == result:
        print("Missing Operation = +")
    elif num1 - num2 == result:
        print("Missing Operation = -")
    elif num1 * num2 == result:
        print("Missing Operation = *")
    else:
        print("No valid operation found.")

missingoperation()