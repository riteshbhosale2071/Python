def adjacentangleclassification():
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))

    if angle1 <= 0 or angle2 <= 0:
        print("Angles must be positive.")
        return

    total = angle1 + angle2

    print("Sum of Angles:", total, "°")

    if total == 90:
        print("Classification: Complementary Adjacent Angles")
    elif total == 180:
        print("Classification: Supplementary Adjacent Angles / Linear Pair")
    elif angle1 == angle2:
        print("Classification: Equal Adjacent Angles")
    else:
        print("Classification: General Adjacent Angles")

adjacentangleclassification()