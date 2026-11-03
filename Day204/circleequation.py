def circleequation():
    center_x = float(input("Enter the center X-coordinate (h): "))
    center_y = float(input("Enter the center Y-coordinate (k): "))
    radius = float(input("Enter the radius of the circle: "))

    if radius <= 0:
        print("Invalid radius. Radius must be positive.")
        return

    radius_squared = radius ** 2

    def format_value(value):
        return f"{value:g}"

    h = format_value(center_x)
    k = format_value(center_y)
    r_squared = format_value(radius_squared)

    if center_x == 0:
        x_part = "x"
    elif center_x < 0:
        x_part = f"(x + {format_value(abs(center_x))})"
    else:
        x_part = f"(x - {h})"

    if center_y == 0:
        y_part = "y"
    elif center_y < 0:
        y_part = f"(y + {format_value(abs(center_y))})"
    else:
        y_part = f"(y - {k})"

    print(f"Center: ({h}, {k})")
    print(f"Radius: {format_value(radius)}")
    print(f"Circle Equation: {x_part}^2 + {y_part}^2 = {r_squared}")

circleequation()