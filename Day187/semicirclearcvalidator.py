def semicirclearcvalidator():
    print("Semicircle Arc Validator :")

    radius = float(input("Enter the semicircle radius: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    import math

    diameter = 2 * radius
    arc_length = math.pi * radius
    circumference = 2 * math.pi * radius
    sector_area = (math.pi * radius ** 2) / 2

    print("\nSemicircle Measurements :")
    print("Radius:", round(radius, 2))
    print("Diameter:", round(diameter, 2))
    print("Semicircular Arc Length:", round(arc_length, 4))
    print("Semicircle Area:", round(sector_area, 4))
    print("Full Circle Circumference:", round(circumference, 4))

    angle = float(input("\nEnter the given arc angle in degrees: "))

    if angle < 0 or angle > 360:
        print("Arc angle must be between 0 and 360 degrees.")
        return

    print("\nArc Validation :")
    print("Given Arc Angle:", round(angle, 2), "degrees")

    if abs(angle - 180) < 0.000001:
        print("Validation Status: VALID")
        print("The arc is a semicircle.")
    else:
        print("Validation Status: INVALID")
        print("A semicircular arc must measure 180 degrees.")

    given_arc_length = (angle / 360) * circumference
    print("Given Arc Length:", round(given_arc_length, 4))

    if abs(given_arc_length - arc_length) < 0.000001:
        print("Arc Length Check: PASSED")
    else:
        print("Arc Length Check: FAILED")

semicirclearcvalidator()