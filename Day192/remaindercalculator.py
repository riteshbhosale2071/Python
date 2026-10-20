def remaindercalculator():
    print("Remainder Calculator :")

    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))
    except ValueError:
        print("Invalid input! Please enter integers.")
        return

    if divisor == 0:
        print("Error: Division by zero is not allowed.")
        return

    quotient = dividend // divisor
    remainder = dividend % divisor

    print("\nCalculation Results :")
    print("Dividend:", dividend)
    print("Divisor:", divisor)
    print("Quotient:", quotient)
    print("Remainder:", remainder)

    print("\nVerification :")
    print("Dividend = Divisor × Quotient + Remainder")
    print(
        dividend, "=", divisor, "×", quotient, "+", remainder
    )

    if dividend == divisor * quotient + remainder:
        print("Verification: Correct")
    else:
        print("Verification: Incorrect")

    if remainder == 0:
        print("Result: The dividend is exactly divisible by the divisor.")
    else:
        print("Result: The division leaves a remainder.")

    print("Absolute Remainder:", abs(remainder))

remaindercalculator()