def samebaseindex():
    base = int(input("Enter the base: "))
    exponent1 = int(input("Enter the first exponent: "))
    exponent2 = int(input("Enter the second exponent: "))

    result_exponent = exponent1 + exponent2

    print("Simplified Expression:")
    print(f"{base}^{exponent1} × {base}^{exponent2} = {base}^{result_exponent}")

samebaseindex()