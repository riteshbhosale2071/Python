def centralangletoarc():
    print("Central Angle to Arc Analyzer :")

    radius = float(input("Enter circle radius: "))
    angle = float(input("Enter central angle in degrees: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    if angle < 0 or angle > 360:
        print("Central angle must be between 0 and 360 degrees.")
        return

    import math

    circumference = 2 * math.pi * radius
    arc_length = (angle / 360) * circumference
    sector_area = (angle / 360) * math.pi * radius ** 2

    print("\nArc Analysis Results :")
    print("Circle Radius:", round(radius, 2))
    print("Central Angle:", round(angle, 2), "degrees")
    print("Full Circumference:", round(circumference, 4))
    print("Arc Length:", round(arc_length, 4))
    print("Sector Area:", round(sector_area, 4))

    if angle == 0:
        print("Arc Type: Zero-length arc")
    elif angle < 180:
        print("Arc Type: Minor arc")
    elif angle == 180:
        print("Arc Type: Semicircle")
    elif angle < 360:
        print("Arc Type: Major arc")
    else:
        print("Arc Type: Full circle")

    print("Arc Percentage of Circle:", round((angle / 360) * 100, 2), "%")

centralangletoarc()