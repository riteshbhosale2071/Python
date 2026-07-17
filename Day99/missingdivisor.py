def finddivisor():
    dividend = int(input("Enter dividend: "))
    quotient = int(input("Enter quotient: "))

    if quotient == 0:
        print("Quotient cannot be zero.")
        return

    divisor = dividend // quotient
    print("Missing Divisor =", divisor)

finddivisor()