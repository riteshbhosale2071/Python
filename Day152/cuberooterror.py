def cuberooterror():
    print("Cube Root Error Checker :")

    number = float(input("Enter the number: "))
    given_root = float(input("Enter the claimed cube root: "))

    calculated_value = given_root ** 3

    if number >= 0:
        actual_root = number ** (1 / 3)
    else:
        actual_root = -((-number) ** (1 / 3))

    print("\nCube Root Error Analysis :")
    print("Number:", number)
    print("Claimed Cube Root:", given_root)
    print("Cube of Claimed Root:", calculated_value)
    print("Actual Cube Root:", actual_root)

    tolerance = 1e-9

    if abs(calculated_value - number) < tolerance:
        print("\nResult: Correct.")
        print("The claimed cube root is valid.")
    else:
        error = abs(calculated_value - number)

        print("\nResult: Error Detected.")
        print("Absolute Error:", error)
        print("Correct Cube Root:", actual_root)

cuberooterror()