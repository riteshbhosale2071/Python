def trianglemissingbase():
    area = float(input("Enter the area of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    if area <= 0 or height <= 0:
        print("Area and height must be positive.")
        return

    base = (2 * area) / height

    print("Missing Base:", base)

trianglemissingbase()