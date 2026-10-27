def linearpairangle():
    print("Linear Pair Angle Calculator")
    print("1. Find the second angle")
    print("2. Check whether two angles form a linear pair")

    choice = input("Enter your choice: ")

    if choice == "1":
        angle1 = float(input("Enter the first angle in degrees: "))

        if 0 <= angle1 <= 180:
            angle2 = 180 - angle1
            print("Second angle:", angle2, "degrees")
        else:
            print("Invalid angle. Enter an angle between 0 and 180.")

    elif choice == "2":
        angle1 = float(input("Enter the first angle in degrees: "))
        angle2 = float(input("Enter the second angle in degrees: "))

        if 0 <= angle1 <= 180 and 0 <= angle2 <= 180:
            if abs(angle1 + angle2 - 180) < 0.000001:
                print("The angles form a linear pair if they are adjacent.")
            else:
                print("The angles do not form a linear pair.")
        else:
            print("Invalid angles. Enter angles between 0 and 180.")

    else:
        print("Invalid choice.")

linearpairangle()