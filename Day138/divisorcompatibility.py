def divisorcompatibility():
    number = int(input("Enter the number: "))
    divisor1 = int(input("Enter first divisor: "))
    divisor2 = int(input("Enter second divisor: "))

    if divisor1 == 0 or divisor2 == 0:
        print("Divisors cannot be zero.")
        return

    divisible_by_first = number % divisor1 == 0
    divisible_by_second = number % divisor2 == 0

    if divisible_by_first and divisible_by_second:
        print("The number is divisible by both divisors.")
    elif divisible_by_first:
        print("The number is divisible only by the first divisor.")
    elif divisible_by_second:
        print("The number is divisible only by the second divisor.")
    else:
        print("The number is not divisible by either divisor.")

divisorcompatibility()