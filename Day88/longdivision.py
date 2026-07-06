def longdivide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor

    print("Dividend :", dividend)
    print("Divisor  :", divisor)
    print("Quotient :", quotient)
    print("Remainder:", remainder)

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

longdivide(dividend, divisor)