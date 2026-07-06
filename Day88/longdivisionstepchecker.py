def longdivisionsteps(dividend, divisor):
    quotient = dividend // divisor
    product = quotient * divisor
    remainder = dividend - product

    print("Dividend :", dividend)
    print("Divisor  :", divisor)
    print("Quotient :", quotient)
    print("Step 1: Multiply =", quotient, "*", divisor, "=", product)
    print("Step 2: Subtract =", dividend, "-", product, "=", remainder)

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

longdivisionsteps(dividend, divisor)