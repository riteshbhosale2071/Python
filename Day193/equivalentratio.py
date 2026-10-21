def equivalentratio():
    print("Equivalent Ratio :")

    try:
        a = int(input("Enter the first term of the ratio: "))
        b = int(input("Enter the second term of the ratio: "))
        n = int(input("Enter the number of equivalent ratios to generate: "))
    except ValueError:
        print("Invalid input! Please enter integers.")
        return

    if a < 0 or b < 0:
        print("Ratio terms cannot be negative.")
        return

    if a == 0 and b == 0:
        print("The ratio 0:0 is undefined.")
        return

    if n <= 0:
        print("Number of ratios must be greater than zero.")
        return

    print("\nGenerated Equivalent Ratios :")
    print("Original Ratio:", str(a) + ":" + str(b))

    for multiplier in range(1, n + 1):
        first = a * multiplier
        second = b * multiplier

        print(
            "Multiplier:", multiplier,
            "| Equivalent Ratio:", str(first) + ":" + str(second)
        )

    print("\nVerification :")

    for multiplier in range(1, n + 1):
        first = a * multiplier
        second = b * multiplier

        if a * second == b * first:
            print(str(first) + ":" + str(second), "- Valid equivalent ratio")
        else:
            print(str(first) + ":" + str(second), "- Not equivalent")

    print("\nRatio Analysis :")

    if a == b:
        print("The original ratio is 1:1 or an equivalent ratio of 1:1.")
    elif a == 0:
        print("All generated ratios represent a zero-to-positive ratio.")
    elif b == 0:
        print("All generated ratios represent a positive-to-zero ratio.")
    else:
        print("All generated ratios preserve the original proportion.")

    print("Total Ratios Generated:", n)

equivalentratio()