def squareroottypechecker():
    print("Square Root Type Checker :")

    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    print("\nSquare Root Analysis :")
    print("Entered Number:", number)

    if number < 0:
        print("Classification: Negative Number")
        print("Its square root is not a real number.")
        print("Complex Square Root:", round(abs(number) ** 0.5, 4), "i")
        return

    square_root = number ** 0.5

    print("Square Root:", round(square_root, 6))

    if number == int(number):
        integer_number = int(number)
        root_integer = int(square_root)

        if root_integer * root_integer == integer_number:
            print("Classification: Perfect Square")
            print("Square Root Type: Integer")
        else:
            print("Classification: Non-Perfect Square")
            print("Square Root Type: Irrational")
    else:
        numerator = int(number * 1000000)
        denominator = 1000000

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

        root_numerator = int(numerator ** 0.5)
        root_denominator = int(denominator ** 0.5)

        if (root_numerator ** 2 == numerator and
                root_denominator ** 2 == denominator):
            print("Classification: Rational Number")
            print("Square Root Type: Rational")
        else:
            print("Classification: Decimal Number")
            print("Square Root Type: Depends on the exact value.")

    if number == 0:
        print("Special Case: The square root of zero is zero.")
    elif number == 1:
        print("Special Case: The square root of one is one.")

squareroottypechecker()