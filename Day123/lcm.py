def lcm():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    prime_factors = {}

    for number in numbers:
        number = abs(number)
        divisor = 2
        factors = {}

        while number > 1:
            if number % divisor == 0:
                factors[divisor] = factors.get(divisor, 0) + 1
                number //= divisor
            else:
                divisor += 1

        for prime, count in factors.items():
            prime_factors[prime] = max(
                prime_factors.get(prime, 0), count
            )

    lcm = 1

    for prime, count in prime_factors.items():
        lcm *= prime ** count

    print("Prime Factors Used:", prime_factors)
    print("LCM:", lcm)

lcm()