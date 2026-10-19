def fractionsimplifier():
    print("Fraction Simplifier :")

    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
    except ValueError:
        print("Invalid input! Please enter integers.")
        return

    if denominator == 0:
        print("Error: Denominator cannot be zero.")
        return

    original_numerator = numerator
    original_denominator = denominator

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
        simplified_numerator = numerator // gcd
        simplified_denominator = denominator // gcd
    else:
        simplified_numerator = 0
        simplified_denominator = 1

    print("\nSimplification Results :")
    print("Original Fraction:",
          str(original_numerator) + "/" + str(original_denominator))
    print("Greatest Common Divisor:", gcd)
    print("Simplified Fraction:",
          str(simplified_numerator) + "/" + str(simplified_denominator))

    if simplified_denominator == 1:
        print("Simplified Value:", simplified_numerator)
    else:
        print("Decimal Value:",
              round(simplified_numerator / simplified_denominator, 4))

    if original_numerator == 0:
        print("Result: The fraction is zero.")
    elif simplified_denominator == 1:
        print("Result: The fraction represents an integer.")
    elif gcd == 1:
        print("Result: The fraction is already in its simplest form.")
    else:
        print("Result: The fraction has been simplified successfully.")

fractionsimplifier()