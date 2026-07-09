def orderfractions():
    num1 = int(input("Enter numerator of first fraction: "))
    den1 = int(input("Enter denominator of first fraction: "))

    num2 = int(input("Enter numerator of second fraction: "))
    den2 = int(input("Enter denominator of second fraction: "))

    value1 = num1 / den1
    value2 = num2 / den2

    if value1 < value2:
        print("Ascending Order:")
        print(num1, "/", den1, ",", num2, "/", den2)
    elif value2 < value1:
        print("Ascending Order:")
        print(num2, "/", den2, ",", num1, "/", den1)
    else:
        print("Both fractions are equal.")

orderfractions()