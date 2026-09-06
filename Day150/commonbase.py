import math 
def commonbase():
    print("Common Base Converter :")

    base1 = float(input("Enter first base: "))
    exponent1 = int(input("Enter first exponent: "))

    base2 = float(input("Enter second base: "))
    exponent2 = int(input("Enter second exponent: "))

    if base1 <= 0 or base2 <= 0:
        print("Bases must be positive.")
        return

    value1 = base1 ** exponent1
    value2 = base2 ** exponent2

    print("\nCommon Base Conversion :")
    print(f"{base1}^{exponent1} =", value1)
    print(f"{base2}^{exponent2} =", value2)

    if abs(value1 - value2) < 1e-9:
        print("The two powers are equal.")
    else:
        print("The two powers are not equal.")

    if base1 != 1 and base2 != 1:
        log_ratio = math.log(base2) / math.log(base1)

        if abs(log_ratio - round(log_ratio)) < 1e-9:
            multiplier = round(log_ratio)
            print(f"\n{base2} can be written as {base1}^{multiplier}.")
            print(
                f"Therefore, {base2}^{exponent2} = "
                f"{base1}^{multiplier * exponent2}."
            )
        else:
            print("\nThe bases cannot be converted to simple integer powers of each other.")

commonbase()