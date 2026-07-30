def missingfraction():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = float(input("Enter the decimal value of the fraction: "))

    calculated = numerator / denominator

    if calculated == result:
        print("The fraction matches the given decimal value.")
    else:
        print("The fraction does not match the given decimal value.")
        print("Actual Decimal Value:", calculated)

missingfraction()