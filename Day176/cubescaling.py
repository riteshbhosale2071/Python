def cubescaling():
    print("Cube Scaling Simulator :")

    side = float(input("Enter original side length: "))
    scale_factor = float(input("Enter scale factor: "))

    if side <= 0 or scale_factor <= 0:
        print("Side length and scale factor must be greater than zero.")
        return

    original_volume = side ** 3
    original_surface_area = 6 * side ** 2

    new_side = side * scale_factor
    new_volume = new_side ** 3
    new_surface_area = 6 * new_side ** 2

    print("\nOriginal Cube :")
    print("Side Length:", round(side, 2))
    print("Surface Area:", round(original_surface_area, 2))
    print("Volume:", round(original_volume, 2))

    print("\nScaled Cube :")
    print("Scale Factor:", round(scale_factor, 2))
    print("New Side Length:", round(new_side, 2))
    print("New Surface Area:", round(new_surface_area, 2))
    print("New Volume:", round(new_volume, 2))

    print("\nChange :")
    print("Surface Area Change:", round(new_surface_area - original_surface_area, 2))
    print("Volume Change:", round(new_volume - original_volume, 2))

cubescaling()