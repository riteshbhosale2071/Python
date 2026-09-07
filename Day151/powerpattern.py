import math

def powerpattern():
    print("Power Pattern Search :")

    n = int(input("Enter the number of values: "))

    if n < 2:
        print("Enter at least 2 values.")
        return

    values = []

    for i in range(n):
        value = float(input(f"Enter value {i + 1}: "))

        if value <= 0:
            print("Please enter positive values only.")
            return

        values.append(value)

    print("\nPower Pattern Search :")
    print("Values:", values)

    ratios = []

    for i in range(1, n):
        ratios.append(values[i] / values[i - 1])

    if all(abs(ratios[i] - ratios[0]) < 1e-9 for i in range(1, len(ratios))):
        print("Power pattern detected.")
        print("Common multiplier:", ratios[0])
    else:
        print("No constant power pattern detected.")

    print("\nCommon Base Search :")

    found = False

    for base in range(2, 11):
        exponents = []

        for value in values:
            exponent = round(math.log(value, base))

            if abs(base ** exponent - value) < 1e-9:
                exponents.append(exponent)
            else:
                break

        if len(exponents) == n:
            print(f"Common base found: {base}")
            print("Exponents:", exponents)
            found = True
            break

    if not found:
        print("No common integer base found.")

powerpattern()