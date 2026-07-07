def remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor

    print("Quotient :", quotient)
    print("Remainder:", remainder)

    if remainder == 0:
        print("The number is exactly divisible.")
    else:
        print("The number is not exactly divisible.")

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

remainder(dividend, divisor)