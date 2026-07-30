def fractionsequence():
    numerator = int(input("Enter the starting numerator: "))
    denominator = int(input("Enter the denominator: "))
    terms = int(input("Enter the number of terms: "))

    print("Fraction Sequence:")

    for i in range(terms):
        print(numerator + i, "/", denominator)

fractionsequence()