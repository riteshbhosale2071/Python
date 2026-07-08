def mixedtoimproper():
    whole = int(input("Enter whole number: "))
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    improper_numerator = (whole * denominator) + numerator

    print("Improper Fraction:", improper_numerator, "/", denominator)

mixedtoimproper()