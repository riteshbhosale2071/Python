def commonfactors():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Common Factors are:")

    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            print(i)

commonfactors()