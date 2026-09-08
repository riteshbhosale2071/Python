def smallestdivisorforperfectcube():
    print("Smallest Divisor for Perfect Cube :")

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

    divisor_needed = 1

    for factor, power in factors:
        remainder = power % 3

        if remainder != 0:
            divisor_needed *= factor ** remainder

    quotient = original // divisor_needed

    print("\nPerfect Cube Analysis :")
    print("Original Number:", original)

    print("Prime Factorization:")
    for factor, power in factors:
        print(f"{factor}^{power}")

    print("\nSmallest Divisor:", divisor_needed)
    print("Quotient:", quotient)

    if divisor_needed == 1:
        print("The number is already a perfect cube.")
    else:
        cube_root = round(quotient ** (1 / 3))
        print(f"{original} ÷ {divisor_needed} = {quotient}")
        print(f"{quotient} = {cube_root}³")

smallestdivisorforperfectcube()