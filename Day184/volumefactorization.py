def volumefactorization():
    print("Volume Factorization :")

    volume = int(input("Enter the volume of the cuboid: "))

    if volume <= 0:
        print("Volume must be a positive integer.")
        return

    factors = []

    for length in range(1, volume + 1):
        if volume % length == 0:
            remaining = volume // length

            for width in range(length, remaining + 1):
                if remaining % width == 0:
                    height = remaining // width

                    if width <= height:
                        factors.append((length, width, height))

    print("\nVolume Factorization Results :")

    for i in range(len(factors)):
        length, width, height = factors[i]
        print(
            i + 1, ".",
            length, "x", width, "x", height,
            "=", length * width * height
        )

    print("\nTotal Dimension Combinations:", len(factors))

    print("\nPrime Factorization :")
    number = volume
    divisor = 2
    prime_factors = []

    while number > 1:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1

    print("Prime Factors:", prime_factors)

    expression = ""
    for i in range(len(prime_factors)):
        if i == 0:
            expression = str(prime_factors[i])
        else:
            expression += " x " + str(prime_factors[i])

    print("Factorized Form:", expression)

volumefactorization()