def find():
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    a = num
    b = den

    while b != 0:
        a, b = b, a % b

    hcf = a
    num = num // hcf
    den = den // hcf

    print("Simplified Fraction =", num, "/", den)

find()