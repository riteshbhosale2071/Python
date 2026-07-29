def improperfraction():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    whole = numerator // denominator
    remainder = numerator % denominator

    print("Improper Fraction:", numerator, "/", denominator)
    print("Whole Part:", whole)
    print("Remainder:", remainder)

    if remainder == 0:
        print("This is a whole number.")
    else:
        print("Mixed Fraction:", whole, remainder, "/", denominator)

improperfraction()