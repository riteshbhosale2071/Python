def clock():
    hour = int(input("Enter hour (1-12): "))
    minute = int(input("Enter minutes (0-59): "))

    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 6

    angle = abs(hour_angle - minute_angle)

    if angle > 180:
        angle = 360 - angle

    print("\nClock Angle Report")
    print("-" * 30)
    print("Hour Hand Angle =", hour_angle, "degrees")
    print("Minute Hand Angle =", minute_angle, "degrees")
    print("Smallest Angle =", round(angle, 2), "degrees")

    if angle < 90:
        print("Angle Type = Acute")
    elif angle == 90:
        print("Angle Type = Right")
    elif angle < 180:
        print("Angle Type = Obtuse")
    elif angle == 180:
        print("Angle Type = Straight")

clock()