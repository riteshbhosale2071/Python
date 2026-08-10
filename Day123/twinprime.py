def twinprime():
    start = int(input("Enter the lower limit: "))
    end = int(input("Enter the upper limit: "))

    def is_prime(number):
        if number < 2:
            return False

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False

        return True

    twin_primes = []

    for number in range(max(2, start), end - 1):
        if is_prime(number) and is_prime(number + 2):
            twin_primes.append((number, number + 2))

    print("Twin Prime Pairs:", twin_primes)

twinprime()