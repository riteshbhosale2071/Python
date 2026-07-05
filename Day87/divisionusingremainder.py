def division(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor

    print("Quotient:", quotient)
    print("Remainder:", remainder)


num1 = int(input("Enter dividend: "))
num2 = int(input("Enter divisor: "))

division(num1, num2)