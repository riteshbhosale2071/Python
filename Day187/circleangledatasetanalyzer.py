def circleangledatasetanalyzer():
    print("Circle Angle Dataset Analyzer :")

    number = int(input("Enter the number of angle measurements: "))

    if number <= 0:
        print("Number of measurements must be greater than zero.")
        return

    angles = []
    total = 0

    for i in range(number):
        angle = float(input("Enter angle " + str(i + 1) + " in degrees: "))

        if angle < 0 or angle > 360:
            print("Invalid angle. Enter a value between 0 and 360 degrees.")
            return

        angles.append(angle)
        total += angle

    average = total / number
    smallest = min(angles)
    largest = max(angles)

    sorted_angles = sorted(angles)
    middle = number // 2

    if number % 2 == 0:
        median = (sorted_angles[middle - 1] + sorted_angles[middle]) / 2
    else:
        median = sorted_angles[middle]

    print("\nDataset Analysis :")
    print("Total Measurements:", number)
    print("Sum of Angles:", round(total, 2), "degrees")
    print("Average Angle:", round(average, 2), "degrees")
    print("Median Angle:", round(median, 2), "degrees")
    print("Smallest Angle:", round(smallest, 2), "degrees")
    print("Largest Angle:", round(largest, 2), "degrees")
    print("Angle Range:", round(largest - smallest, 2), "degrees")

    print("\nAngle Classification :")

    minor = 0
    right = 0
    straight = 0
    reflex = 0
    full = 0
    zero = 0

    for angle in angles:
        if angle == 0:
            zero += 1
        elif angle < 90:
            minor += 1
        elif angle == 90:
            right += 1
        elif angle == 180:
            straight += 1
        elif angle < 360:
            reflex += 1
        else:
            full += 1

    print("Zero Angles:", zero)
    print("Acute Angles:", minor)
    print("Right Angles:", right)
    print("Straight Angles:", straight)
    print("Reflex Angles:", reflex)
    print("Full Angles:", full)

    if abs(total - 360) < 0.000001:
        print("\nSum Check: The angles total exactly one full circle.")
    elif total < 360:
        print("\nSum Check: Remaining angle =", round(360 - total, 2), "degrees")
    else:
        print("\nSum Check: Total exceeds one full circle by", round(total - 360, 2), "degrees")

    print("\nSorted Angles:", sorted_angles)

circleangledatasetanalyzer()