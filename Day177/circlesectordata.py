def circlesectordata():
    print("Circle Sector Data Analyzer :")

    radius = float(input("Enter radius of the circle: "))
    angle = float(input("Enter sector angle in degrees: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    if angle <= 0 or angle > 360:
        print("Angle must be between 0 and 360 degrees.")
        return

    pi = 3.14159

    area = pi * radius ** 2
    sector_area = (angle / 360) * area
    arc_length = (angle / 360) * 2 * pi * radius
    perimeter = 2 * radius + arc_length

    print("\nSector Data :")
    print("Radius:", round(radius, 2))
    print("Sector Angle:", round(angle, 2), "degrees")
    print("Circle Area:", round(area, 2))
    print("Sector Area:", round(sector_area, 2))
    print("Arc Length:", round(arc_length, 2))
    print("Sector Perimeter:", round(perimeter, 2))

    if angle < 90:
        print("Sector Type: Acute Sector")
    elif angle == 90:
        print("Sector Type: Quadrant")
    elif angle < 180:
        print("Sector Type: Obtuse Sector")
    elif angle == 180:
        print("Sector Type: Semicircle")
    else:
        print("Sector Type: Major Sector")

circlesectordata()