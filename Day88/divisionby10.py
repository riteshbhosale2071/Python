def dividebyten(number):
    quotient = number // 10
    remainder = number % 10

    print("Quotient:", quotient)
    print("Remainder:", remainder)

num = int(input("Enter a number: "))

dividebyten(num)