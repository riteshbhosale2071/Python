def triangleanglesum():
    print("Triangle Angle Sum Calculator")
    print("1. Calculate the third angle")
    print("2. Check triangle angles")

    choice = input("Enter your choice: ")

    if choice == "1":
        angle1 = float(input("Enter the first angle: "))
        angle2 = float(input("Enter the second angle: "))

        if 0 < angle1 < 180 and 0 < angle2 < 180:
            angle3 = 180 - angle1 - angle2

            if angle3 > 0:
                print("Third angle:", angle3, "degrees")
            else:
                print("These angles cannot form a triangle.")
        else:
            print("Invalid angles.")

    elif choice == "2":
        angle1 = float(input("Enter the first angle: "))
        angle2 = float(input("Enter the second angle: "))
        angle3 = float(input("Enter the third angle: "))

        if angle1 > 0 and angle2 > 0 and angle3 > 0:
            if abs(angle1 + angle2 + angle3 - 180) < 0.000001:
                print("The angles can form a triangle.")
            else:
                print("The angles cannot form a triangle.")
        else:
            print("All angles must be greater than zero.")

    else:
        print("Invalid choice.")

triangleanglesum()