def mixedfractioncalculator():
    whole = int(input("Enter the whole number: "))
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    improper_numerator = whole * denominator + numerator

    print("Improper Fraction:", improper_numerator, "/", denominator)

mixedfractioncalculator()