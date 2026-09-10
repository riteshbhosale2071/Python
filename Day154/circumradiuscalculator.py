def circumradiuscalculator():
    print("Circumradius Calculator :")

    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle.")
        return

    s = (a + b + c) / 2

    area_square = s * (s - a) * (s - b) * (s - c)

    if area_square <= 0:
        print("Unable to calculate circumradius.")
        return

    area = area_square ** 0.5

    radius = (a * b * c) / (4 * area)

    print("Circumradius: {:.2f}".format(radius))

circumradiuscalculator()