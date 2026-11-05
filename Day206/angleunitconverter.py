import math

def angleunitconverter():
    print("Angle Unit Converter")
    print("1. Degrees to Radians")
    print("2. Radians to Degrees")
    print("3. Degrees to Gradians")
    print("4. Gradians to Degrees")

    choice = input("Enter your choice (1-4): ")

    try:
        angle = float(input("Enter the angle value: "))

        if choice == "1":
            result = math.radians(angle)
            print("Angle in radians:", round(result, 4))

        elif choice == "2":
            result = math.degrees(angle)
            print("Angle in degrees:", round(result, 4))

        elif choice == "3":
            result = angle * (200 / 180)
            print("Angle in gradians:", round(result, 4))

        elif choice == "4":
            result = angle * (180 / 200)
            print("Angle in degrees:", round(result, 4))

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    except ValueError:
        print("Please enter a valid numeric angle.")

angleunitconverter()