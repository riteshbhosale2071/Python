def findremainder(dividend, divisor, quotient):
    remainder = dividend - (divisor * quotient)
    print("Missing Remainder:", remainder)

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
quotient = int(input("Enter quotient: "))

findremainder(dividend, divisor, quotient)