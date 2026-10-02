def cubevolumefromsurfacearea():
    print("Cube Volume from Surface Area :")

    surface_area = float(input("Enter surface area of the cube: "))

    if surface_area <= 0:
        print("Surface area must be greater than zero.")
        return

    side = (surface_area / 6) ** 0.5
    volume = side ** 3

    print("\nSurface Area:", round(surface_area, 2))
    print("Side Length:", round(side, 2))
    print("Volume:", round(volume, 2))

cubevolumefromsurfacearea()