def angle():
    angle = float(input("Enter the angle(less than 180):"))

    if angle > 0 and angle < 90:
        print("Angle is Acute")
    
    elif angle == 90:
        print("Angle is Right")

    elif angle > 90 and angle < 180:
        print("Angle is Obtuse")

    else:
        print("Invalid Angle")

angle()