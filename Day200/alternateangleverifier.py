def alternateangleverifier():
    print("Alternate Angle Verifier")
    print("1. Verify alternate interior angles")
    print("2. Verify alternate exterior angles")

    choice = input("Enter your choice: ")

    if choice == "1":
        angle1 = float(input("Enter the first interior angle: "))
        angle2 = float(input("Enter the second interior angle: "))

        if 0 <= angle1 <= 180 and 0 <= angle2 <= 180:
            if abs(angle1 - angle2) < 0.000001:
                print("The angles are equal and may be alternate interior angles.")
            else:
                print("The angles are not equal.")
        else:
            print("Invalid angles.")

    elif choice == "2":
        angle1 = float(input("Enter the first exterior angle: "))
        angle2 = float(input("Enter the second exterior angle: "))

        if 0 <= angle1 <= 180 and 0 <= angle2 <= 180:
            if abs(angle1 - angle2) < 0.000001:
                print("The angles are equal and may be alternate exterior angles.")
            else:
                print("The angles are not equal.")
        else:
            print("Invalid angles.")

    else:
        print("Invalid choice.")

alternateangleverifier()