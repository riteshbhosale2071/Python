def quadrilateralclassification():
    print("Quadrilateral Classification Engine :")

    sides = []
    for i in range(4):
        side = float(input("Enter side " + str(i + 1) + ": "))
        sides.append(side)

    angle1 = float(input("Enter angle 1: "))
    angle2 = float(input("Enter angle 2: "))
    angle3 = float(input("Enter angle 3: "))
    angle4 = float(input("Enter angle 4: "))

    total = angle1 + angle2 + angle3 + angle4

    if total != 360:
        print("Invalid quadrilateral.")
        return

    if sides[0] == sides[1] and sides[1] == sides[2] and sides[2] == sides[3]:
        if angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 == 90:
            print("Classification: Square")
        else:
            print("Classification: Rhombus")

    elif sides[0] == sides[2] and sides[1] == sides[3]:
        if angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 == 90:
            print("Classification: Rectangle")
        else:
            print("Classification: Parallelogram")

    elif sides[0] == sides[1] and sides[2] == sides[3]:
        print("Classification: Kite")

    else:
        print("Classification: General Quadrilateral")

quadrilateralclassification()