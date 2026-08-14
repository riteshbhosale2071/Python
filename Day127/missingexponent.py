def missingexponent():
    base = int(input("Enter the base: "))
    result = int(input("Enter the result: "))

    if base <= 0 or base == 1 or result <= 0:
        print("Enter a valid base (greater than 1) and positive result.")
        return

    exponent = 0
    value = 1

    while value < result:
        value *= base
        exponent += 1

    if value == result:
        print("Missing Exponent:", exponent)
    else:
        print("No whole-number exponent exists.")

missingexponent()