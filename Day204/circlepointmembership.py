import math

def circlepointmembership():
    center_x = float(input("Enter the circle center X-coordinate: "))
    center_y = float(input("Enter the circle center Y-coordinate: "))
    radius = float(input("Enter the radius of the circle: "))

    point_x = float(input("Enter the point X-coordinate: "))
    point_y = float(input("Enter the point Y-coordinate: "))

    if radius <= 0:
        print("Invalid radius. Radius must be positive.")
        return

    distance = math.sqrt(
        (point_x - center_x) ** 2 +
        (point_y - center_y) ** 2
    )

    print(f"Distance from center: {distance:.2f}")

    if math.isclose(distance, radius, rel_tol=1e-9, abs_tol=1e-9):
        print("The point lies on the circle.")
    elif distance < radius:
        print("The point lies inside the circle.")
    else:
        print("The point lies outside the circle.")

circlepointmembership()