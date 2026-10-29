def supplementaryangle():
    print("Supplementary Angle Checker")
    print("1. Find the supplementary angle")
    print("2. Check two supplementary angles")

    choice = input("Enter your choice: ")

    if choice == "1":
        angle = float(input("Enter the angle in degrees: "))

        if 0 <= angle <= 180:
            supplementary = 180 - angle
            print("Supplementary angle:", supplementary, "degrees")
        else:
            print("Invalid angle. Enter a value between 0 and 180.")

    elif choice == "2":
        angle1 = float(input("Enter the first angle: "))
        angle2 = float(input("Enter the second angle: "))

        if 0 <= angle1 <= 180 and 0 <= angle2 <= 180:
            if abs(angle1 + angle2 - 180) < 0.000001:
                print("The angles are supplementary.")
            else:
                print("The angles are not supplementary.")
        else:
            print("Invalid angles. Enter values between 0 and 180.")

    else:
        print("Invalid choice.")

supplementaryangle()