def angleinteriorexterior():
    print("Enter the two ray directions and the point direction.")
    print("All directions should be measured in degrees from 0° to 360°.")

    ray1 = float(input("Enter direction of first ray: ")) % 360
    ray2 = float(input("Enter direction of second ray: ")) % 360
    point = float(input("Enter direction of point: ")) % 360

    angle = (ray2 - ray1) % 360

    if angle > 180:
        ray1, ray2 = ray2, ray1
        angle = 360 - angle

    point_angle = (point - ray1) % 360

    if point_angle == 0 or point_angle == angle:
        print("The point lies ON the angle.")
    elif point_angle < angle:
        print("The point lies INSIDE the angle.")
    else:
        print("The point lies OUTSIDE the angle.")

angleinteriorexterior()