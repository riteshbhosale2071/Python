def verify_division(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor

    if dividend == (divisor * quotient) + remainder:
        print("Division is Correct")
    else:
        print("Division is Incorrect")

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

verify_division(dividend, divisor)