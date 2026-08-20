def trianglemissingheight():
    area = float(input("Enter the area of the triangle: "))
    base = float(input("Enter the base of the triangle: "))

    if area <= 0 or base <= 0:
        print("Area and base must be positive.")
        return

    height = (2 * area) / base

    print("Missing Height:", height)

trianglemissingheight()