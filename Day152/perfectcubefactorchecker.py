def perfectcubefactorchecker():
    print("Perfect Cube Factor Checker :")

    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return

    original = number
    factors = []

    # Find prime factors
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

    print("\nFactor Analysis :")

    for factor, power in factors:
        print(f"{factor}^{power}")

    is_perfect_cube = all(power % 3 == 0 for factor, power in factors)

    if is_perfect_cube:
        cube_root = 1

        for factor, power in factors:
            cube_root *= factor ** (power // 3)

        print("\nResult: The number is a Perfect Cube.")
        print(f"{original} = {cube_root}³")
        print("Cube Root:", cube_root)
    else:
        print("\nResult: The number is NOT a Perfect Cube.")
        print("At least one prime factor has an exponent that is not divisible by 3.")

perfectcubefactorchecker()