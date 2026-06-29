def fractioncomparison():
    numerator1 = int(input("Enter numerator of first fraction: "))
    denominator1 = int(input("Enter denominator of first fraction: "))

    numerator2 = int(input("Enter numerator of second fraction: "))
    denominator2 = int(input("Enter denominator of second fraction: "))

    value1 = numerator1 * denominator2
    value2 = numerator2 * denominator1

    if value1 > value2:
        print(f"{numerator1}/{denominator1} is greater than {numerator2}/{denominator2}")

    elif value1 < value2:
        print(f"{numerator2}/{denominator2} is greater than {numerator1}/{denominator1}")

    else:
        print("Both fractions are equal")

fractioncomparison()