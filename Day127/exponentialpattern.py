def exponentialpattern():
    base = float(input("Enter the base: "))
    terms = int(input("Enter the number of terms: "))

    if terms <= 0:
        print("Number of terms must be positive.")
        return

    print("Exponential Pattern:")

    for exponent in range(terms):
        value = base ** exponent
        print(f"{base}^{exponent} = {value}")

exponentialpattern()