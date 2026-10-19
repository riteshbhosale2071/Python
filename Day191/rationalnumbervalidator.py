def rationalnumbervalidator():
    print("Rational Number Validator :")

    numerator = input("Enter the numerator: ")
    denominator = input("Enter the denominator: ")

    try:
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        print("Invalid input! Numerator and denominator must be integers.")
        return

    if denominator == 0:
        print("Invalid rational number: Denominator cannot be zero.")
        return

    print("\nValidation Results :")
    print("Numerator:", numerator)
    print("Denominator:", denominator)

    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    a = abs(numerator)
    b = denominator

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    gcd = a

    if gcd != 0:
        numerator //= gcd
        denominator //= gcd

    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    print("Valid Rational Number: Yes")
    print("Simplified Form:", str(numerator) + "/" + str(denominator))
    print("Decimal Value:", numerator / denominator)

    if denominator == 1:
        print("Classification: Integer")
    else:
        print("Classification: Non-integer rational number")

    if numerator == 0:
        print("The rational number is zero.")
    elif numerator > 0:
        print("The rational number is positive.")
    else:
        print("The rational number is negative.")

rationalnumbervalidator()