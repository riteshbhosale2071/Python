import math

def conemeasurementcalculator():
    print("Cone Measurement Calculator")
    print("1. Calculate Volume")
    print("2. Calculate Curved Surface Area")
    print("3. Calculate Total Surface Area")
    print("4. Calculate Slant Height")
    print("5. Calculate Base Area")

    choice = input("Enter your choice (1-5): ")

    try:
        radius = float(input("Enter radius of cone: "))
        height = float(input("Enter height of cone: "))

        if radius <= 0 or height <= 0:
            print("Radius and height must be greater than zero.")
            return

        slant_height = math.sqrt(radius ** 2 + height ** 2)

        if choice == "1":
            result = (math.pi * radius ** 2 * height) / 3
            print("Volume:", round(result, 2), "cubic units")

        elif choice == "2":
            result = math.pi * radius * slant_height
            print("Curved Surface Area:", round(result, 2), "square units")

        elif choice == "3":
            result = math.pi * radius * (radius + slant_height)
            print("Total Surface Area:", round(result, 2), "square units")

        elif choice == "4":
            print("Slant Height:", round(slant_height, 2), "units")

        elif choice == "5":
            result = math.pi * radius ** 2
            print("Base Area:", round(result, 2), "square units")

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    except ValueError:
        print("Please enter valid numeric values.")

conemeasurementcalculator()