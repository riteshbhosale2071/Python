def cuberoottable():
    print("Cube Root Table Generator :")

    start = int(input("Enter starting integer: "))
    end = int(input("Enter ending integer: "))
    decimal_places = int(input("Enter decimal places: "))

    if start > end:
        print("Starting value must be less than or equal to ending value.")
        return

    if decimal_places < 0:
        print("Decimal places cannot be negative.")
        return

    print("\nCube Root Table :")
    print(f"{'Number':<12}{'Cube Root':<15}")
    print("-" * 27)

    for number in range(start, end + 1):
        if number >= 0:
            cube_root = number ** (1 / 3)
        else:
            cube_root = -((-number) ** (1 / 3))

        print(f"{number:<12}{cube_root:<15.{decimal_places}f}")

cuberoottable()