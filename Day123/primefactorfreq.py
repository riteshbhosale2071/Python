def primefactorfrequency():
    number = int(input("Enter a number: "))

    if number < 2:
        print("Prime factors do not exist for this number.")
        return

    factors = {}
    divisor = 2

    while number > 1:
        if number % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            number //= divisor
        else:
            divisor += 1

    print("Prime Factor Frequency:")
    for prime, count in factors.items():
        print(prime, "occurs", count, "time(s)")

primefactorfrequency()