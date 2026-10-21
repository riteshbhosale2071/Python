def ratiosimplification():
    print("Ratio Simplification :")

    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter integers.")
        return

    if a == 0 and b == 0:
        print("The ratio 0:0 is undefined.")
        return

    if a < 0 or b < 0:
        print("Negative values are not supported in this ratio tool.")
        return

    x = a
    y = b

    while y != 0:
        remainder = x % y
        x = y
        y = remainder

    gcd = x

    if gcd != 0:
        simplified_a = a // gcd
        simplified_b = b // gcd
    else:
        simplified_a = a
        simplified_b = b

    print("\nRatio Simplification Results :")
    print("Original Ratio:", str(a) + ":" + str(b))
    print("Greatest Common Divisor:", gcd)
    print("Simplified Ratio:", str(simplified_a) + ":" + str(simplified_b))

    print("\nRatio Analysis :")

    if a == b:
        print("Both numbers are equal.")
    elif a > b:
        print("The first number is greater than the second.")
    else:
        print("The second number is greater than the first.")

    if b != 0:
        print("Ratio as a Decimal:", round(a / b, 4))
    else:
        print("Ratio as a Decimal: Undefined because the second number is zero.")

    if simplified_a == 0 or simplified_b == 0:
        print("The simplified ratio contains zero.")
    elif simplified_a == 1 and simplified_b == 1:
        print("The ratio simplifies to 1:1.")
    else:
        print("The ratio is in its simplest form.")

    print("\nVerification :")
    print("First Number Divided by GCD:", a // gcd if gcd != 0 else 0)
    print("Second Number Divided by GCD:", b // gcd if gcd != 0 else 0)

ratiosimplification()