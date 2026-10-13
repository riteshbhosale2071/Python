def shapemeasurements(shape):
    if shape == "Cube":
        side = float(input("Enter cube side length: "))
        if side <= 0:
            return None
        volume = side ** 3
        surface_area = 6 * side ** 2

    elif shape == "Cuboid":
        length = float(input("Enter cuboid length: "))
        width = float(input("Enter cuboid width: "))
        height = float(input("Enter cuboid height: "))

        if length <= 0 or width <= 0 or height <= 0:
            return None

        volume = length * width * height
        surface_area = 2 * (
            length * width + width * height + length * height
        )

    elif shape == "Sphere":
        radius = float(input("Enter sphere radius: "))
        if radius <= 0:
            return None

        volume = (4 / 3) * 3.14159 * radius ** 3
        surface_area = 4 * 3.14159 * radius ** 2

    elif shape == "Cylinder":
        radius = float(input("Enter cylinder radius: "))
        height = float(input("Enter cylinder height: "))

        if radius <= 0 or height <= 0:
            return None

        volume = 3.14159 * radius ** 2 * height
        surface_area = 2 * 3.14159 * radius * (radius + height)

    else:
        return None

    return [shape, volume, surface_area]


def shapecomparisonengine():
    print("3D Shape Comparison Engine :")
    print("Available Shapes: Cube, Cuboid, Sphere, Cylinder")

    number = int(input("Enter the number of shapes to compare: "))

    if number < 2:
        print("Enter at least two shapes for comparison.")
        return

    shapes = []

    for i in range(number):
        print("\nShape", i + 1)
        shape_name = input("Enter shape name: ").strip().title()

        if shape_name not in ["Cube", "Cuboid", "Sphere", "Cylinder"]:
            print("Invalid shape name. Please restart the program.")
            return

        result = shapemeasurements(shape_name)

        if result is None:
            print("Invalid dimensions. All dimensions must be positive.")
            return

        shapes.append(result)

    print("\nShape Comparison Results :")

    for i in range(number):
        print("\nShape:", shapes[i][0])
        print("Volume:", round(shapes[i][1], 2), "cubic units")
        print("Surface Area:", round(shapes[i][2], 2), "square units")
        print(
            "Volume-to-Surface Ratio:",
            round(shapes[i][1] / shapes[i][2], 4)
        )

    largest_volume = max(shapes, key=lambda item: item[1])
    smallest_volume = min(shapes, key=lambda item: item[1])
    largest_surface = max(shapes, key=lambda item: item[2])
    smallest_surface = min(shapes, key=lambda item: item[2])

    print("\nFinal Comparison :")
    print("Largest Volume:", largest_volume[0])
    print("Volume:", round(largest_volume[1], 2))
    print("Smallest Volume:", smallest_volume[0])
    print("Volume:", round(smallest_volume[1], 2))
    print("Largest Surface Area:", largest_surface[0])
    print("Area:", round(largest_surface[2], 2))
    print("Smallest Surface Area:", smallest_surface[0])
    print("Area:", round(smallest_surface[2], 2))

    shapes.sort(key=lambda item: item[1], reverse=True)

    print("\nVolume Ranking :")
    for i in range(number):
        print(
            i + 1, ".",
            shapes[i][0],
            "- Volume:",
            round(shapes[i][1], 2)
        )

shapecomparisonengine()