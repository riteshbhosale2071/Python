def circlegeometryreasoning():
    print("Circle Geometry Reasoning Engine :")

    radius = float(input("Enter radius of the circle: "))
    chord_length = float(input("Enter chord length: "))
    central_angle = float(input("Enter central angle in degrees: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    if chord_length <= 0 or chord_length > 2 * radius:
        print("Chord length must be greater than zero and not exceed the diameter.")
        return

    if central_angle <= 0 or central_angle > 360:
        print("Central angle must be between 0 and 360 degrees.")
        return

    pi = 3.14159

    diameter = 2 * radius
    circumference = 2 * pi * radius
    circle_area = pi * radius ** 2

    half_chord = chord_length / 2
    distance_from_center = (radius ** 2 - half_chord ** 2) ** 0.5

    arc_length = (central_angle / 360) * circumference
    sector_area = (central_angle / 360) * circle_area

    print("\nCircle Geometry Analysis :")
    print("Radius:", round(radius, 2))
    print("Diameter:", round(diameter, 2))
    print("Circumference:", round(circumference, 2))
    print("Circle Area:", round(circle_area, 2))
    print("Chord Length:", round(chord_length, 2))
    print("Distance from Center to Chord:", round(distance_from_center, 2))
    print("Arc Length:", round(arc_length, 2))
    print("Sector Area:", round(sector_area, 2))

    print("\nReasoning Results :")

    if abs(chord_length - diameter) < 0.000001:
        print("The chord is a diameter.")
    else:
        print("The chord is not a diameter.")

    if distance_from_center < radius:
        print("The chord lies inside the circle.")

    if central_angle < 180:
        print("The given arc is a minor arc.")
    elif central_angle == 180:
        print("The given arc is a semicircle.")
    else:
        print("The given arc is a major arc.")

    if central_angle == 360:
        print("The sector represents the complete circle.")
    elif central_angle == 180:
        print("The sector represents half of the circle.")
    elif central_angle < 180:
        print("The sector represents less than half of the circle.")
    else:
        print("The sector represents more than half of the circle.")

circlegeometryreasoning()