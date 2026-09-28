def congruenceerrordetector():
    print("Congruence Error Detector :")

    print("\nChoose the congruence rule:")
    print("1. SSS")
    print("2. SAS")
    print("3. ASA")
    print("4. RHS")

    rule = int(input("Enter the rule number: "))

    if rule == 1:
        side1 = float(input("Enter first corresponding side of Triangle 1: "))
        side2 = float(input("Enter first corresponding side of Triangle 2: "))
        side3 = float(input("Enter second corresponding side of Triangle 1: "))
        side4 = float(input("Enter second corresponding side of Triangle 2: "))
        side5 = float(input("Enter third corresponding side of Triangle 1: "))
        side6 = float(input("Enter third corresponding side of Triangle 2: "))

        if side1 != side2:
            print("Error: First pair of corresponding sides is not equal.")
        elif side3 != side4:
            print("Error: Second pair of corresponding sides is not equal.")
        elif side5 != side6:
            print("Error: Third pair of corresponding sides is not equal.")
        else:
            print("No error found. Congruence is valid by SSS.")

    elif rule == 2:
        side1 = float(input("Enter first side of Triangle 1: "))
        side2 = float(input("Enter first side of Triangle 2: "))
        angle1 = float(input("Enter included angle of Triangle 1: "))
        angle2 = float(input("Enter included angle of Triangle 2: "))
        side3 = float(input("Enter second side of Triangle 1: "))
        side4 = float(input("Enter second side of Triangle 2: "))

        if side1 != side2:
            print("Error: First pair of corresponding sides is not equal.")
        elif angle1 != angle2:
            print("Error: Included angles are not equal.")
        elif side3 != side4:
            print("Error: Second pair of corresponding sides is not equal.")
        else:
            print("No error found. Congruence is valid by SAS.")

    elif rule == 3:
        angle1 = float(input("Enter first angle of Triangle 1: "))
        angle2 = float(input("Enter first angle of Triangle 2: "))
        side1 = float(input("Enter included side of Triangle 1: "))
        side2 = float(input("Enter included side of Triangle 2: "))
        angle3 = float(input("Enter second angle of Triangle 1: "))
        angle4 = float(input("Enter second angle of Triangle 2: "))

        if angle1 != angle2:
            print("Error: First pair of corresponding angles is not equal.")
        elif side1 != side2:
            print("Error: Included sides are not equal.")
        elif angle3 != angle4:
            print("Error: Second pair of corresponding angles is not equal.")
        else:
            print("No error found. Congruence is valid by ASA.")

    elif rule == 4:
        hypotenuse1 = float(input("Enter hypotenuse of Triangle 1: "))
        hypotenuse2 = float(input("Enter hypotenuse of Triangle 2: "))
        side1 = float(input("Enter corresponding side of Triangle 1: "))
        side2 = float(input("Enter corresponding side of Triangle 2: "))

        if hypotenuse1 != hypotenuse2:
            print("Error: Hypotenuses are not equal.")
        elif side1 != side2:
            print("Error: Corresponding sides are not equal.")
        else:
            print("No error found. Congruence is valid by RHS.")

    else:
        print("Invalid rule number.")

congruenceerrordetector()