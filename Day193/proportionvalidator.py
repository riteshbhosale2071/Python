def proportionvalidator():
    print("Proportion Validator :")

    try:
        a = float(input("Enter the first term (a): "))
        b = float(input("Enter the second term (b): "))
        c = float(input("Enter the third term (c): "))
        d = float(input("Enter the fourth term (d): "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    print("\nProportion Analysis :")
    print("First Ratio:", str(a) + ":" + str(b))
    print("Second Ratio:", str(c) + ":" + str(d))

    if b == 0 or d == 0:
        print("Cannot validate the proportion because a denominator is zero.")
        return

    first_ratio = a / b
    second_ratio = c / d

    print("First Ratio Value:", round(first_ratio, 6))
    print("Second Ratio Value:", round(second_ratio, 6))

    left_product = a * d
    right_product = b * c

    print("\nCross-Multiplication Test :")
    print("a × d =", left_product)
    print("b × c =", right_product)

    if abs(left_product - right_product) < 1e-9:
        print("Result: The four numbers form a valid proportion.")
        print("Therefore, a/b = c/d.")
    else:
        print("Result: The four numbers do not form a proportion.")
        print("Therefore, a/b is not equal to c/d.")

    difference = first_ratio - second_ratio

    print("\nAdditional Results :")
    print("Difference Between Ratios:", round(difference, 6))
    print("Absolute Difference:", round(abs(difference), 6))

    if abs(difference) < 1e-9:
        print("Both ratios are equivalent.")
    else:
        print("Both ratios are different.")

    if a == b and c == d:
        print("Both ratios are equal to 1.")
    elif a == 0 and c == 0:
        print("Both ratios are zero.")

proportionvalidator()