def fractioncomparison():
    num1 = int(input("Enter numerator of first fraction: "))
    den1 = int(input("Enter denominator of first fraction: "))

    num2 = int(input("Enter numerator of second fraction: "))
    den2 = int(input("Enter denominator of second fraction: "))

    value1 = num1 * den2
    value2 = num2 * den1

    if value1 > value2:
        print("First fraction is greater.")
    elif value1 < value2:
        print("Second fraction is greater.")
    else:
        print("Both fractions are equal.")

fractioncomparison()