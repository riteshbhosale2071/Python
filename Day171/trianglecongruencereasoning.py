def trianglecongruencereasoning():
    print("Triangle Congruence Reasoning Engine :")

    print("\nEnter the available information:")
    print("1. Three corresponding sides are equal")
    print("2. Two corresponding sides and included angle are equal")
    print("3. Two corresponding angles and included side are equal")
    print("4. Right triangles with equal hypotenuse and one corresponding side")
    print("5. Insufficient information")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        side1 = float(input("Enter first side pair value: "))
        side2 = float(input("Enter second side pair value: "))
        side3 = float(input("Enter third side pair value: "))

        if side1 > 0 and side2 > 0 and side3 > 0:
            print("\nReasoning:")
            print("Three corresponding sides are equal.")
            print("Therefore, the triangles are congruent by SSS.")
        else:
            print("Invalid side measurements.")

    elif choice == 2:
        side1 = float(input("Enter first corresponding side: "))
        side2 = float(input("Enter second corresponding side: "))
        angle = float(input("Enter included angle: "))

        if side1 > 0 and side2 > 0 and angle > 0 and angle < 180:
            print("\nReasoning:")
            print("Two corresponding sides and the included angle are given.")
            print("Therefore, the triangles are congruent by SAS.")
        else:
            print("Invalid measurements.")

    elif choice == 3:
        angle1 = float(input("Enter first corresponding angle: "))
        angle2 = float(input("Enter second corresponding angle: "))
        side = float(input("Enter included side: "))

        if angle1 > 0 and angle2 > 0 and angle1 < 180 and angle2 < 180 and side > 0:
            print("\nReasoning:")
            print("Two corresponding angles and the included side are given.")
            print("Therefore, the triangles are congruent by ASA.")
        else:
            print("Invalid measurements.")

    elif choice == 4:
        hypotenuse1 = float(input("Enter hypotenuse of Triangle 1: "))
        hypotenuse2 = float(input("Enter hypotenuse of Triangle 2: "))
        side1 = float(input("Enter corresponding side of Triangle 1: "))
        side2 = float(input("Enter corresponding side of Triangle 2: "))

        if hypotenuse1 == hypotenuse2 and side1 == side2 and hypotenuse1 > side1:
            print("\nReasoning:")
            print("Both triangles are right triangles with equal hypotenuses and one equal side.")
            print("Therefore, the triangles are congruent by RHS.")
        else:
            print("The given information does not satisfy RHS.")

    elif choice == 5:
        print("\nReasoning:")
        print("There is not enough information to prove triangle congruence.")
        print("More corresponding sides or angles are required.")

    else:
        print("Invalid choice.")

trianglecongruencereasoning()