def complementarypair():
    angle1 = float(input("Enter the first angle: "))

    if angle1 <= 0 or angle1 >= 90:
        print("Angle must be between 0° and 90°.")
        return

    angle2 = 90 - angle1

    print("Complementary Angle Pair:")
    print("First Angle:", angle1, "°")
    print("Second Angle:", angle2, "°")
    print("Sum:", angle1 + angle2, "°")

complementarypair()