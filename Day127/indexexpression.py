def indexexpression():
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))

    if base == 0 and exponent <= 0:
        print("Invalid expression.")
        return

    result = base ** exponent

    print("Index Expression:", f"{base}^{exponent}")
    print("Result:", result)

indexexpression()