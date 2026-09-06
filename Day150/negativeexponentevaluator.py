def negativeexponentevaluator():
    print("Negative Exponent Evaluator :")

    base = float(input("Enter the base: "))
    exponent = int(input("Enter a negative exponent: "))

    if base == 0 and exponent < 0:
        print("Zero cannot have a negative exponent.")
        return

    if exponent >= 0:
        print("Please enter a negative exponent.")
        return

    result = base ** exponent

    print("\nResult :")
    print("Base:", base)
    print("Exponent:", exponent)
    print("Value:", result)

negativeexponentevaluator()