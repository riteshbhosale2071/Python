def commonfactorextractor():
    print("Common Factor Extractor :")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    smaller = a
    if b < smaller:
        smaller = b

    common_factor = 1

    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            common_factor = i

    print("Greatest common factor =", common_factor)
    print("Common factor form =", common_factor, "*", a // common_factor, "and", common_factor, "*", b // common_factor)

commonfactorextractor()