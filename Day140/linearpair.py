def linearpair():
    angle1 = float(input("Enter the first angle: "))

    if angle1 <= 0 or angle1 >= 180:
        print("Angle must be between 0° and 180°.")
        return

    angle2 = 180 - angle1

    print("Linear Pair Angles:")
    print("First Angle:", angle1, "°")
    print("Second Angle:", angle2, "°")
    print("Sum:", angle1 + angle2, "°")

linearpair()