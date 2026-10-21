def continuedproportion():
    print("Continued Proportion Checker :")

    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))
        c = float(input("Enter the third number (c): "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    print("\nContinued Proportion Analysis :")
    print("First Number:", a)
    print("Second Number:", b)
    print("Third Number:", c)

    if a == 0 or b == 0:
        print("Cannot check continued proportion because a denominator is zero.")
        return

    first_ratio = b / a
    second_ratio = c / b

    print("First Ratio (b/a):", round(first_ratio, 6))
    print("Second Ratio (c/b):", round(second_ratio, 6))

    if abs(first_ratio - second_ratio) < 1e-9:
        print("Result: The numbers are in continued proportion.")
        print("Therefore, a : b = b : c.")
    else:
        print("Result: The numbers are not in continued proportion.")

    print("\nVerification :")

    left_product = b * b
    right_product = a * c

    print("b² =", left_product)
    print("a × c =", right_product)

    if abs(left_product - right_product) < 1e-9:
        print("Verified: b² = a × c.")
        print("The continued proportion is valid.")
    else:
        print("Not verified: b² is not equal to a × c.")

    print("\nAdditional Analysis :")

    if a != 0:
        geometric_mean_squared = a * c

        if geometric_mean_squared >= 0:
            geometric_mean = geometric_mean_squared ** 0.5
            print("Square Root of a × c:", round(geometric_mean, 6))
        else:
            print("a × c is negative, so its square root is not real.")

    if a == b == c:
        print("All three numbers are equal.")
    elif a == b or b == c:
        print("At least two consecutive numbers are equal.")
    else:
        print("The three numbers are not all equal.")

continuedproportion()