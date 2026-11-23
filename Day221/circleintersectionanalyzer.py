import math

def circleintersectionanalyzer():
    print("Circle Intersection Analyzer")

    print("\nEnter details of the first circle:")
    x1 = float(input("Enter centre x-coordinate: "))
    y1 = float(input("Enter centre y-coordinate: "))
    r1 = float(input("Enter radius: "))

    print("\nEnter details of the second circle:")
    x2 = float(input("Enter centre x-coordinate: "))
    y2 = float(input("Enter centre y-coordinate: "))
    r2 = float(input("Enter radius: "))

    if r1 <= 0 or r2 <= 0:
        print("Circle radii must be positive.")
        return

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("\nCircle Intersection Analysis:")
    print("Distance between centres =", round(distance, 4))
    print("Sum of radii =", round(r1 + r2, 4))
    print("Difference of radii =", round(abs(r1 - r2), 4))

    if math.isclose(distance, 0, abs_tol=1e-9) and math.isclose(r1, r2, rel_tol=1e-9):
        print("Result: Circles are coincident.")
        print("They have infinitely many common points.")

    elif math.isclose(distance, 0, abs_tol=1e-9):
        print("Result: Circles are concentric.")
        print("They have no common points.")

    elif distance > r1 + r2:
        print("Result: Circles are externally separate.")
        print("They have no intersection points.")

    elif math.isclose(distance, r1 + r2, rel_tol=1e-9):
        print("Result: Circles touch externally.")
        print("They have one common point.")

    elif distance < abs(r1 - r2):
        print("Result: One circle lies inside the other.")
        print("They have no intersection points.")

    elif math.isclose(distance, abs(r1 - r2), rel_tol=1e-9):
        print("Result: Circles touch internally.")
        print("They have one common point.")

    else:
        print("Result: Circles intersect at two distinct points.")

circleintersectionanalyzer()