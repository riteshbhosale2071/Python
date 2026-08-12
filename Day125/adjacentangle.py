def adjacentangle():
    angle1 = float(input("Enter the first angle in degrees: "))
    angle2 = float(input("Enter the second angle in degrees: "))

    if angle1 <= 0 or angle2 <= 0:
        print("Angles must be positive.")
    elif angle1 + angle2 < 180:
        print("The angles can be adjacent.")
    elif angle1 + angle2 == 180:
        print("The angles are adjacent supplementary angles.")
    else:
        print("The angles cannot form adjacent angles.")

adjacentangle()