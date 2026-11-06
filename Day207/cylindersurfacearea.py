import math

def cylindersurfacearea():
    print("Cylinder Surface Area Calculator")
    print("1. Calculate Curved Surface Area")
    print("2. Calculate Total Surface Area")
    print("3. Calculate Base Area")
    print("4. Calculate Volume")

    choice = input("Enter your choice (1-4): ")

    try:
        radius = float(input("Enter radius of cylinder: "))
        height = float(input("Enter height of cylinder: "))

        if radius <= 0 or height <= 0:
            print("Radius and height must be greater than zero.")
            return

        if choice == "1":
            result = 2 * math.pi * radius * height
            print("Curved Surface Area:", round(result, 2), "square units")

        elif choice == "2":
            result = 2 * math.pi * radius * (radius + height)
            print("Total Surface Area:", round(result, 2), "square units")

        elif choice == "3":
            result = math.pi * radius ** 2
            print("Base Area:", round(result, 2), "square units")

        elif choice == "4":
            result = math.pi * radius ** 2 * height
            print("Volume:", round(result, 2), "cubic units")

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    except ValueError:
        print("Please enter valid numeric values.")

cylindersurfacearea()