def fractionobjects():
    total_objects = int(input("Enter total number of objects: "))
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = (total_objects * numerator) // denominator

    print("Fraction:", numerator, "/", denominator)
    print("Fraction of Objects:", result)

fractionobjects()