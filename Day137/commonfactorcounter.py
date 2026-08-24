def commonfactorcounter():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 == 0 or num2 == 0:
        print("Please enter non-zero integers.")
        return

    count = 0

    for i in range(1, min(abs(num1), abs(num2)) + 1):
        if num1 % i == 0 and num2 % i == 0:
            count += 1

    print("Number of Common Factors:", count)

commonfactorcounter()