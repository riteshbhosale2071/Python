def finddivisor(dividend, quotient, remainder):
    divisor = (dividend - remainder) // quotient
    print("Missing Divisor:", divisor)

dividend = int(input("Enter dividend: "))
quotient = int(input("Enter quotient: "))
remainder = int(input("Enter remainder: "))

finddivisor(dividend, quotient, remainder)