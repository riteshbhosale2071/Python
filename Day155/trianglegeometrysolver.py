def trianglegeometrysolver():
    print("Triangle Geometry Solver :")

    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Sides must be positive.")
        return

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle.")
        return

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    perimeter = a + b + c

    median_a = (2 * b * b + 2 * c * c - a * a) ** 0.5 / 2
    median_b = (2 * a * a + 2 * c * c - b * b) ** 0.5 / 2
    median_c = (2 * a * a + 2 * b * b - c * c) ** 0.5 / 2

    altitude_a = (2 * area) / a
    altitude_b = (2 * area) / b
    altitude_c = (2 * area) / c

    angle_a_value = (b * b + c * c - a * a) / (2 * b * c)
    angle_b_value = (a * a + c * c - b * b) / (2 * a * c)
    angle_c_value = (a * a + b * b - c * c) / (2 * a * b)

    print("\n-Triangle Geometry Results :")
    print("Perimeter: {:.2f}".format(perimeter))
    print("Semi-perimeter: {:.2f}".format(s))
    print("Area: {:.2f}".format(area))

    print("\n Median Lengths :")
    print("Median to side a: {:.2f}".format(median_a))
    print("Median to side b: {:.2f}".format(median_b))
    print("Median to side c: {:.2f}".format(median_c))

    print("\nAltitudes :")
    print("Altitude to side a: {:.2f}".format(altitude_a))
    print("Altitude to side b: {:.2f}".format(altitude_b))
    print("Altitude to side c: {:.2f}".format(altitude_c))

    if a == b and b == c:
        print("\nTriangle Type: Equilateral")
    elif a == b or b == c or a == c:
        print("\nTriangle Type: Isosceles")
    else:
        print("\nTriangle Type: Scalene")

    largest = a

    if b > largest:
        largest = b
    if c > largest:
        largest = c

    if largest == a:
        other1 = b
        other2 = c
    elif largest == b:
        other1 = a
        other2 = c
    else:
        other1 = a
        other2 = b

    if largest * largest == other1 * other1 + other2 * other2:
        print("Angle Type: Right-Angled")
    elif largest * largest < other1 * other1 + other2 * other2:
        print("Angle Type: Acute-Angled")
    else:
        print("Angle Type: Obtuse-Angled")

    print("\nGeometry calculations completed successfully.")

trianglegeometrysolver()