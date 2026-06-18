def carry():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    carry = 0
    count = 0

    while num1 > 0 or num2 > 0:

        digit1 = num1 % 10
        digit2 = num2 % 10

        total = digit1 + digit2 + carry

        if total >= 10:
            carry = 1
            count += 1
        else:
            carry = 0

        num1 //= 10
        num2 //= 10

    print("Total Carries =", count)

carry()