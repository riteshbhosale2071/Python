def missingdividend(divisor, quotient, remainder):
    dividend = (divisor * quotient) + remainder
    print("Missing Dividend:", dividend)

divisor = int(input("Enter divisor: "))
quotient = int(input("Enter quotient: "))
remainder = int(input("Enter remainder: "))

missingdividend(divisor, quotient, remainder)