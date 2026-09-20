def kitepropertyanalyzer():
    print("Kite Property Analyzer :")

    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))
    side4 = float(input("Enter side 4: "))

    diagonal1 = float(input("Enter diagonal 1: "))
    diagonal2 = float(input("Enter diagonal 2: "))

    if side1 > 0 and side2 > 0 and side3 > 0 and side4 > 0:
        if side1 == side2 and side3 == side4:
            print("Two pairs of adjacent sides are equal.")

            if diagonal1 > 0 and diagonal2 > 0:
                print("Diagonal 1 =", diagonal1)
                print("Diagonal 2 =", diagonal2)

                if diagonal1 != diagonal2:
                    print("The diagonals may have different lengths.")

                print("The given shape satisfies the basic kite property.")
            else:
                print("Diagonal lengths must be greater than zero.")
        else:
            print("The adjacent sides are not equal.")
            print("The shape does not satisfy the basic kite property.")
    else:
        print("Side lengths must be greater than zero.")

kitepropertyanalyzer()