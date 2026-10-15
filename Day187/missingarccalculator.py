def missingarccalculator():
    print("Missing Arc Calculator :")

    number = int(input("Enter the number of known arcs: "))

    if number <= 0:
        print("Number of known arcs must be greater than zero.")
        return

    total_angle = 0

    for i in range(number):
        angle = float(input("Enter angle of arc " + str(i + 1) + " in degrees: "))

        if angle < 0 or angle > 360:
            print("Each arc angle must be between 0 and 360 degrees.")
            return

        total_angle += angle

    if total_angle > 360:
        print("Invalid input: Known arc angles exceed 360 degrees.")
        print("Total known angle:", round(total_angle, 2), "degrees")
        return

    missing_angle = 360 - total_angle

    print("\nMissing Arc Results :")
    print("Total Known Arc Angle:", round(total_angle, 2), "degrees")
    print("Missing Arc Angle:", round(missing_angle, 2), "degrees")

    if missing_angle == 0:
        print("All arcs together cover the complete circle.")
    else:
        print("Percentage of Circle Missing:", round(missing_angle / 360 * 100, 2), "%")

    radius = float(input("\nEnter circle radius to calculate missing arc length: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    import math

    circumference = 2 * math.pi * radius
    missing_arc_length = (missing_angle / 360) * circumference

    print("Circle Circumference:", round(circumference, 4))
    print("Missing Arc Length:", round(missing_arc_length, 4))

missingarccalculator()