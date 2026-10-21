def ratioconsistencyanalyzer():
    print("Ratio Consistency Analyzer :")

    try:
        n = int(input("Enter the number of ratios to compare: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n < 2:
        print("Enter at least two ratios for comparison.")
        return

    ratios = []

    for i in range(n):
        print("\nEnter Ratio", i + 1)

        try:
            a = float(input("Enter first term: "))
            b = float(input("Enter second term: "))
        except ValueError:
            print("Invalid input! Enter numeric values.")
            return

        if a < 0 or b < 0:
            print("Ratio terms cannot be negative.")
            return

        if a == 0 and b == 0:
            print("Both terms of a ratio cannot be zero.")
            return

        if b == 0:
            print("The second term cannot be zero.")
            return

        ratios.append((a, b))

    print("\nRatio Analysis :")

    first_a, first_b = ratios[0]
    reference_value = first_a / first_b
    consistent = True

    for i, ratio in enumerate(ratios):
        a, b = ratio
        value = a / b

        print("\nRatio", i + 1, ":", a, ":", b)
        print("Ratio Value:", round(value, 4))

        if abs(value - reference_value) < 0.000001:
            print("Consistent with the first ratio.")
        else:
            print("Not consistent with the first ratio.")
            consistent = False

    print("\nConsistency Result :")

    if consistent:
        print("All ratios are equivalent and consistent.")
    else:
        print("The ratios are not all equivalent.")

    print("\nPairwise Comparison :")

    for i in range(n):
        for j in range(i + 1, n):
            a1, b1 = ratios[i]
            a2, b2 = ratios[j]

            if abs((a1 / b1) - (a2 / b2)) < 0.000001:
                print("Ratio", i + 1, "and Ratio", j + 1,
                      "are equivalent.")
            else:
                print("Ratio", i + 1, "and Ratio", j + 1,
                      "are not equivalent.")

ratioconsistencyanalyzer()