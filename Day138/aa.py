def remainderconditionchecker():
    number = int(input("Enter the number: "))
    divisor = int(input("Enter the divisor: "))
    required_remainder = int(input("Enter the required remainder: "))

    if divisor <= 0:
        print("Divisor must be positive.")
        return

    if required_remainder < 0 or required_remainder >= divisor:
        print("Invalid remainder. It must be between 0 and divisor - 1.")
        return

    actual_remainder = number % divisor

    print("Actual Remainder:", actual_remainder)

    if actual_remainder == required_remainder:
        print("The remainder condition is satisfied.")
    else:
        print("The remainder condition is not satisfied.")

remainderconditionchecker()