def fractionsubtraction():
    numerator1 = int(input("Enter numerator of first fraction: "))
    denominator1 = int(input("Enter denominator of first fraction: "))

    numerator2 = int(input("Enter numerator of second fraction: "))
    denominator2 = int(input("Enter denominator of second fraction: "))

    numerator = (numerator1 * denominator2) - (numerator2 * denominator1)
    denominator = denominator1 * denominator2

    hcf = 1
    for i in range(1, min(abs(numerator), denominator) + 1):
        if numerator % i == 0 and denominator % i == 0:
            hcf = i

    numerator //= hcf
    denominator //= hcf

    print("Difference =", numerator, "/", denominator)

fractionsubtraction()