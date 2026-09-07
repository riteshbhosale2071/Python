import math

def commonpower():
    print("Common Power Finder :")

    n = int(input("Enter number of values: "))

    if n < 2:
        print("Enter at least 2 values.")
        return

    values = []

    for i in range(n):
        value = int(input(f"Enter value {i + 1}: "))

        if value <= 0:
            print("Please enter positive integers only.")
            return

        values.append(value)

    print("\nCommon Power Analysis :")
    print("Values:", values)

    common_powers = []

    limit = int(math.sqrt(min(values))) + 1

    for base in range(2, limit + 1):
        exponents = []

        for value in values:
            temp = value
            exponent = 0

            while temp % base == 0:
                temp //= base
                exponent += 1

            if temp != 1:
                break

            exponents.append(exponent)

        if len(exponents) == n and all(e > 0 for e in exponents):
            common_powers.append((base, exponents))

    if common_powers:
        print("Common power bases found:")

        for base, exponents in common_powers:
            print(f"\nBase: {base}")
            for i, exponent in enumerate(exponents):
                print(f"{values[i]} = {base}^{exponent}")

    else:
        print("No common integer power base found.")

commonpower()