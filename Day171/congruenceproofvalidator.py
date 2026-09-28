def congruenceproofvalidator():
    print("Congruence Proof Validator :")

    print("\nChoose the congruence rule:")
    print("1. SSS")
    print("2. SAS")
    print("3. ASA")
    print("4. RHS")

    rule = int(input("Enter the rule number: "))

    if rule == 1:
        side1 = float(input("Enter first corresponding side pair: "))
        side2 = float(input("Enter second corresponding side pair: "))
        side3 = float(input("Enter third corresponding side pair: "))

        if side1 == side2 == side3:
            print("Valid proof: Triangles are congruent by SSS.")
        else:
            print("Invalid proof: All three corresponding sides must be equal.")

    elif rule == 2:
        side1 = float(input("Enter first corresponding side pair: "))
        side2 = float(input("Enter second corresponding side pair: "))
        angle1 = float(input("Enter corresponding included angle pair: "))

        if side1 == side2 and angle1 > 0:
            print("Valid proof: Triangles satisfy the SAS measurements.")
        else:
            print("Invalid proof: SAS requires two equal corresponding sides and the included angle.")

    elif rule == 3:
        angle1 = float(input("Enter first corresponding angle pair: "))
        angle2 = float(input("Enter second corresponding angle pair: "))
        side = float(input("Enter corresponding included side pair: "))

        if angle1 == angle2 and side > 0:
            print("Valid proof: Triangles satisfy the ASA measurements.")
        else:
            print("Invalid proof: ASA requires two equal corresponding angles and the included side.")

    elif rule == 4:
        hypotenuse1 = float(input("Enter first hypotenuse pair: "))
        hypotenuse2 = float(input("Enter second hypotenuse pair: "))
        side1 = float(input("Enter corresponding side pair: "))
        side2 = float(input("Enter corresponding side pair for Triangle 2: "))

        if hypotenuse1 == hypotenuse2 and side1 == side2:
            print("Valid proof: Triangles are congruent by RHS.")
        else:
            print("Invalid proof: RHS requires equal hypotenuses and one equal corresponding side.")

    else:
        print("Invalid rule number.")

congruenceproofvalidator()