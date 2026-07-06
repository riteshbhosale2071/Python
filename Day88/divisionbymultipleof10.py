def divide(number, divisor):
    quotient = number // divisor
    remainder = number % divisor

    print("Quotient:", quotient)
    print("Remainder:", remainder)

num = int(input("Enter a number: "))
div = int(input("Enter divisor (10, 100, 1000...): "))

divide(num, div)