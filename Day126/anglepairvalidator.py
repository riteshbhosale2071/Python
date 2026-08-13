def anglepairvalidator():
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))

    if angle1 <= 0 or angle2 <= 0 or angle1 >= 180 or angle2 >= 180:
        print("Invalid angles.")
        return

    print("Angle Sum:", angle1 + angle2, "°")

    if angle1 + angle2 == 90:
        print("The angles are Complementary.")
    elif angle1 + angle2 == 180:
        print("The angles are Supplementary.")
    elif angle1 == angle2:
        print("The angles are Equal.")
    else:
        print("The angles do not form a standard angle pair.")

anglepairvalidator()