def rhombusdiagonalproperty():
    print("Rhombus Diagonal Property Checker :")

    diagonal1 = float(input("Enter diagonal 1: "))
    diagonal2 = float(input("Enter diagonal 2: "))

    angle = float(input("Enter angle between the diagonals: "))

    if diagonal1 > 0 and diagonal2 > 0:
        if angle == 90:
            print("The diagonals are perpendicular.")
            print("The rhombus diagonal property is satisfied.")
        else:
            print("The diagonals are not perpendicular.")
            print("The rhombus diagonal property is not satisfied.")
    else:
        print("Diagonal lengths must be greater than zero.")

rhombusdiagonalproperty()