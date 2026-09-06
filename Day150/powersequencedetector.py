def powersequencedetector():
    print("Power Sequence Detector :")

    n = int(input("Enter number of terms: "))

    if n < 2:
        print("Enter at least 2 terms.")
        return

    terms = []

    for i in range(n):
        value = float(input(f"Enter term {i + 1}: "))

        if value <= 0:
            print("Enter positive values only.")
            return

        terms.append(value)

    power = terms[1] / terms[0]
    is_power_sequence = True

    for i in range(2, n):
        if terms[i - 1] == 0:
            is_power_sequence = False
            break

        current_power = terms[i] / terms[i - 1]

        if abs(current_power - power) > 1e-9:
            is_power_sequence = False
            break

    print("\nPower Sequence Analysis :")
    print("Sequence:", terms)

    if is_power_sequence:
        print("A constant multiplicative pattern is detected.")
        print("Common multiplier:", power)
    else:
        print("No constant power pattern detected.")

powersequencedetector()