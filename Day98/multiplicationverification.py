def verify():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    answer = int(input("Enter multiplication result: "))

    if num1 * num2 == answer:
        print("Correct! Multiplication Verified.")
    else:
        print("Incorrect! Correct Answer =", num1 * num2)

verify()