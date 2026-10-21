def ratiobasederrordetector():
    print("Ratio-Based Error Detector :")

    try:
        n = int(input("Enter the number of ratio comparisons: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of comparisons must be greater than zero.")
        return

    errors = 0

    for i in range(n):
        print("\nComparison", i + 1)

        try:
            a = float(input("Enter first ratio's first term: "))
            b = float(input("Enter first ratio's second term: "))
            c = float(input("Enter second ratio's first term: "))
            d = float(input("Enter second ratio's second term: "))
        except ValueError:
            print("Invalid input! Enter numeric values.")
            return

        if min(a, b, c, d) < 0:
            print("Error: Ratio terms cannot be negative.")
            errors += 1
            continue

        if b == 0 or d == 0:
            print("Error: The second term of a ratio cannot be zero.")
            errors += 1
            continue

        if a == 0 and b == 0 or c == 0 and d == 0:
            print("Error: Both terms of a ratio cannot be zero.")
            errors += 1
            continue

        ratio1 = a / b
        ratio2 = c / d

        print("First Ratio:", a, ":", b)
        print("Second Ratio:", c, ":", d)
        print("First Ratio Value:", round(ratio1, 4))
        print("Second Ratio Value:", round(ratio2, 4))

        if abs(a * d - b * c) < 0.000001:
            print("Result: Ratios are equivalent. No ratio error detected.")
        else:
            print("Result: Ratios are not equivalent.")
            print("Error: The given ratios are inconsistent.")
            errors += 1

    print("\nError Detection Summary :")
    print("Total Comparisons:", n)
    print("Inconsistent or Invalid Comparisons:", errors)
    print("Consistent Comparisons:", n - errors)

    if errors == 0:
        print("All ratio comparisons are valid and consistent.")
    else:
        print("Some ratio comparisons contain errors.")

ratiobasederrordetector()