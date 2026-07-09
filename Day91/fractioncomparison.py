def comparefractions():
    num1 = int(input("Enter numerator of first fraction: "))
    den1 = int(input("Enter denominator of first fraction: "))

    num2 = int(input("Enter numerator of second fraction: "))
    den2 = int(input("Enter denominator of second fraction: "))

    print("\nFirst Fraction : ", end="")
    for i in range(den1):
        if i < num1:
            print("■", end=" ")
        else:
            print("□", end=" ")

    print("\nSecond Fraction:", end=" ")
    for i in range(den2):
        if i < num2:
            print("■", end=" ")
        else:
            print("□", end=" ")

    if num1 / den1 > num2 / den2:
        print("\n\nFirst fraction is greater.")
    elif num1 / den1 < num2 / den2:
        print("\n\nSecond fraction is greater.")
    else:
        print("\n\nBoth fractions are equal.")

comparefractions()