def commondivisor():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    common_divisors = []

    for i in range(1, min(abs(num1), abs(num2)) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)

    print("Common Divisors:", common_divisors)

commondivisor()