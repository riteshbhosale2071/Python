import math

def circletangentvalidator():
    print("Circle Tangent Validator")
    print("1. Verify tangent using radius and tangent length")
    print("2. Verify tangent using centre, external point and contact point")
    print("3. Verify tangent using perpendicular distance")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        radius = float(input("Enter circle radius: "))
        tangent = float(input("Enter tangent length: "))
        distance = float(input("Enter distance from centre to external point: "))

        if radius <= 0 or tangent < 0 or distance <= 0:
            print("Invalid measurements.")
            return

        if math.isclose(distance ** 2, radius ** 2 + tangent ** 2, rel_tol=1e-9):
            print("Valid tangent: The tangent length satisfies the tangent theorem.")
        else:
            print("Invalid tangent: The measurements do not satisfy the tangent theorem.")

    elif choice == "2":
        ox = float(input("Enter centre x-coordinate: "))
        oy = float(input("Enter centre y-coordinate: "))
        px = float(input("Enter external point x-coordinate: "))
        py = float(input("Enter external point y-coordinate: "))
        tx = float(input("Enter contact point x-coordinate: "))
        ty = float(input("Enter contact point y-coordinate: "))

        radius_x = tx - ox
        radius_y = ty - oy
        tangent_x = px - tx
        tangent_y = py - ty

        dot_product = radius_x * tangent_x + radius_y * tangent_y

        if math.isclose(dot_product, 0, abs_tol=1e-9):
            print("Valid tangent: Radius is perpendicular to the tangent.")
        else:
            print("Invalid tangent: Radius is not perpendicular to the tangent.")

    elif choice == "3":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter perpendicular distance from centre to line: "))

        if radius <= 0 or distance < 0:
            print("Invalid measurements.")
            return

        if math.isclose(radius, distance, rel_tol=1e-9):
            print("The line is tangent to the circle.")
        elif distance < radius:
            print("The line is a secant.")
        else:
            print("The line does not intersect the circle.")

    else:
        print("Invalid choice.")

circletangentvalidator()