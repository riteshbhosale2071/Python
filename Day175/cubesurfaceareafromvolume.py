def cubesurfaceareafromvolume():
    print("Cube Surface Area from Volume :")

    volume = float(input("Enter volume of the cube: "))

    if volume <= 0:
        print("Volume must be greater than zero.")
        return

    side = volume ** (1 / 3)
    surface_area = 6 * side * side

    print("\nVolume:", round(volume, 2))
    print("Side Length:", round(side, 2))
    print("Surface Area:", round(surface_area, 2))

cubesurfaceareafromvolume()