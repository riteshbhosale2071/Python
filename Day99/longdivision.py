def long_division():
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    quotient = dividend // divisor
    remainder = dividend % divisor

    print("Dividend :", dividend)
    print("Divisor  :", divisor)
    print("Quotient :", quotient)
    print("Remainder:", remainder)

long_division()