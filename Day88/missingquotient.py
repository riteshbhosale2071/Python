def findquotient(dividend, divisor, remainder):
    quotient = (dividend - remainder) // divisor
    print("Missing Quotient:", quotient)

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
remainder = int(input("Enter remainder: "))

findquotient(dividend, divisor, remainder)