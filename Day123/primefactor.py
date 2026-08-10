def primefactor():
    number = int(input("Enter a number: "))

    if number < 2:
        print("Prime factors do not exist for this number.")
        return

    factors = []
    divisor = 2

    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    print("Prime Factors:", factors)

primefactor()