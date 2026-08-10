def primenumgenerator():
    start = int(input("Enter the lower limit: "))
    end = int(input("Enter the upper limit: "))

    primes = []

    for number in range(max(2, start), end + 1):
        is_prime = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    print("Prime Numbers:", primes)

primenumgenerator()