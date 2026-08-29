def congruentangle():
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))

    if angle1 <= 0 or angle1 >= 360 or angle2 <= 0 or angle2 >= 360:
        print("Angles must be between 0° and 360°.")
        return

    if angle1 == angle2:
        print("The angles are Congruent.")
    else:
        print("The angles are Not Congruent.")

congruentangle()