def cubefactorization():
    print("Cube Factorization Program :")

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

    print("\nCube Factorization :")
    print("Number:", original)

    expression = []

    for factor, power in factors:
        expression.append(f"{factor}^{power}")

    print("Prime Factorization:", " × ".join(expression))

    cube_parts = []
    remaining_parts = []

    for factor, power in factors:
        complete_cubes = power // 3
        remainder = power % 3

        if complete_cubes > 0:
            cube_parts.append(f"{factor}^{complete_cubes * 3}")

        if remainder > 0:
            remaining_parts.append(f"{factor}^{remainder}")

    print("\nCube Groups:")

    if cube_parts:
        print("Complete cube factors:", " × ".join(cube_parts))
    else:
        print("No complete cube factor groups found.")

    if remaining_parts:
        print("Remaining factors:", " × ".join(remaining_parts))
    else:
        print("No remaining factors.")

    is_cube = all(power % 3 == 0 for factor, power in factors)

    if is_cube:
        cube_root = 1

        for factor, power in factors:
            cube_root *= factor ** (power // 3)

        print("\nResult: The number is a perfect cube.")
        print(f"{original} = {cube_root}^3")
    else:
        print("\nResult: The number is not a perfect cube.")

cubefactorization()