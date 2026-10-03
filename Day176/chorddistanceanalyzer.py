def chorddistanceanalyzer():
    print("Chord Distance Analyzer :")

    radius = float(input("Enter radius of the circle: "))
    chord_length = float(input("Enter chord length: "))

    if radius <= 0 or chord_length <= 0:
        print("Radius and chord length must be greater than zero.")
        return

    if chord_length > 2 * radius:
        print("Chord length cannot be greater than the diameter.")
        return

    half_chord = chord_length / 2
    distance = (radius ** 2 - half_chord ** 2) ** 0.5

    diameter = 2 * radius
    angle_radians = 2 * __import__("math").asin(chord_length / diameter)
    angle_degrees = angle_radians * 180 / 3.141592653589793

    print("\nRadius:", round(radius, 2))
    print("Chord Length:", round(chord_length, 2))
    print("Distance from Center to Chord:", round(distance, 2))
    print("Diameter:", round(diameter, 2))
    print("Central Angle:", round(angle_degrees, 2), "degrees")

    if distance == 0:
        print("The chord is a diameter.")
    elif distance < radius:
        print("The chord lies inside the circle.")

chorddistanceanalyzer()