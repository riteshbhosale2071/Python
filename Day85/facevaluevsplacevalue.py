def values():
    number = input("Enter a number (up to 5 digits): ")
    digit = input("Enter the digit to find its Face Value and Place Value: ")

    if digit in number:
        position = number.rindex(digit)
        face_value = int(digit)
        place_value = int(digit) * (10 ** (len(number) - position - 1))

        print("\nFace Value vs Place Value")
        print("-" * 35)
        print("Number =", number)
        print("Digit =", digit)
        print("Face Value =", face_value)
        print("Place Value =", place_value)
    else:
        print("Digit not found in the number.")

values()