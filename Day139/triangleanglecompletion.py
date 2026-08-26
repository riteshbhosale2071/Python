def triangleanglecompletion():
    angle1 = float(input("Enter first angle: "))
    angle2 = float(input("Enter second angle: "))

    if angle1 <= 0 or angle2 <= 0:
        print("Angles must be positive.")
        return

    angle3 = 180 - (angle1 + angle2)

    if angle3 <= 0:
        print("The given angles cannot form a triangle.")
    else:
        print("Missing Third Angle:", angle3, "°")

triangleanglecompletion()