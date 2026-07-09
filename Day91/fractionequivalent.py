def equivalentfraction():
    num1 = int(input("Enter numerator of first fraction: "))
    den1 = int(input("Enter denominator of first fraction: "))

    num2 = int(input("Enter numerator of second fraction: "))
    den2 = int(input("Enter denominator of second fraction: "))

    if num1 * den2 == num2 * den1:
        print("The fractions are Equivalent.")
    else:
        print("The fractions are Not Equivalent.")

equivalentfraction()