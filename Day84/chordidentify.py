def chord():
    radius = float(input("Enter the radius of the circle: "))
    distance = float(input("Enter the distance of the line from the center: "))

    if distance < radius:
        print("\nThe line is a Chord.")
    elif distance == radius:
        print("\nThe line is a Tangent.")
    else:
        print("\nThe line is outside the circle (Not a Chord).")

chord()