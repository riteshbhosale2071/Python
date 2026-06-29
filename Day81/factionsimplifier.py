def fractionsimplifier():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    hcf = 1

    for i in range(1, min(numerator, denominator) + 1):
        if numerator % i == 0 and denominator % i == 0:
            hcf = i

    simple_numerator = numerator // hcf
    simple_denominator = denominator // hcf

    print("Simplified Fraction =", simple_numerator, "/", simple_denominator)

fractionsimplifier()