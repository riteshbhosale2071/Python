import math

def concentriccircleanalyzer():
    center_x1 = float(input("Enter the first circle center X-coordinate: "))
    center_y1 = float(input("Enter the first circle center Y-coordinate: "))
    radius1 = float(input("Enter the first circle radius: "))

    center_x2 = float(input("Enter the second circle center X-coordinate: "))
    center_y2 = float(input("Enter the second circle center Y-coordinate: "))
    radius2 = float(input("Enter the second circle radius: "))

    if radius1 <= 0 or radius2 <= 0:
        print("Invalid radius. Both radii must be positive.")
        return

    if not (
        math.isclose(center_x1, center_x2, abs_tol=1e-9) and
        math.isclose(center_y1, center_y2, abs_tol=1e-9)
    ):
        print("The circles are not concentric.")
        return

    print("The circles are concentric.")

    if math.isclose(radius1, radius2, abs_tol=1e-9):
        print("Both circles have the same radius.")
    else:
        inner_radius = min(radius1, radius2)
        outer_radius = max(radius1, radius2)

        ring_area = math.pi * (outer_radius ** 2 - inner_radius ** 2)

        print(f"Inner Radius: {inner_radius:.2f}")
        print(f"Outer Radius: {outer_radius:.2f}")
        print(f"Area between circles: {ring_area:.2f} square units")

concentriccircleanalyzer()