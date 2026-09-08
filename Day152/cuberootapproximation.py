def cuberootapproximation():
    print("Cube Root Approximation :")

    number = float(input("Enter a number: "))
    decimal_places = int(input("Enter decimal places: "))

    if decimal_places < 0:
        print("Decimal places cannot be negative.")
        return

    if number == 0:
        cube_root = 0.0
    elif number > 0:
        cube_root = number ** (1 / 3)
    else:
        cube_root = -((-number) ** (1 / 3))

    print("\nCube Root Approximation :")
    print("Number:", number)
    print("Approximate Cube Root:", round(cube_root, decimal_places))

    approximation = round(cube_root, decimal_places)
    print("Verification:", approximation, "³ =", approximation ** 3)

cuberootapproximation()