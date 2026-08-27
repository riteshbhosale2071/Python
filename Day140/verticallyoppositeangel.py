def verticallyoppositeangle():
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))

    if angle1 <= 0 or angle1 >= 180 or angle2 <= 0 or angle2 >= 180:
        print("Angles must be between 0° and 180°.")
        return

    if angle1 == angle2:
        print("The angles are Vertically Opposite Angles.")
    else:
        print("The angles are not Vertically Opposite Angles.")

verticallyoppositeangle()