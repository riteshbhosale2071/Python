def findquotient():
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    quotient = dividend // divisor
    print("Missing Quotient =", quotient)

findquotient()