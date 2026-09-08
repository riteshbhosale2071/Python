def smallestmultiplierforperfectcube():
    print("Smallest Multiplier for Perfect Cube :")

    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return

    original = number
    factors = []

    divisor = 2

    while divisor * divisor <= number:
        count = 0

        while number % divisor == 0:
            number //= divisor
            count += 1

        if count > 0:
            factors.append((divisor, count))

        divisor += 1

    if number > 1:
        factors.append((number, 1))

    multiplier = 1

    for factor, power in factors:
        remainder = power % 3

        if remainder != 0:
            multiplier *= factor ** (3 - remainder)

    result = original * multiplier
    cube_root = round(result ** (1 / 3))

    print("\nPerfect Cube Analysis :")
    print("Original Number:", original)

    print("Prime Factorization:")
    for factor, power in factors:
        print(f"{factor}^{power}")

    print("\nSmallest Multiplier:", multiplier)
    print("Resulting Number:", result)
    print("Cube Root:", cube_root)

    if multiplier == 1:
        print("The number is already a perfect cube.")
    else:
        print(f"{original} × {multiplier} = {result}")
        print(f"{result} = {cube_root}³")


smallestmultiplierforperfectcube()