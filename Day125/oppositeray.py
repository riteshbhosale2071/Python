def oppositeray():
    ray1 = float(input("Enter direction of first ray (0-360°): ")) % 360
    ray2 = float(input("Enter direction of second ray (0-360°): ")) % 360

    difference = abs(ray1 - ray2)

    if difference == 180:
        print("The rays are Opposite Rays.")
    else:
        print("The rays are not Opposite Rays.")

oppositeray()