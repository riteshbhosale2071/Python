import math

def hemispheremeasurement():
    print("Hemisphere Measurement Calculator")
    print("1. Calculate Curved Surface Area")
    print("2. Calculate Total Surface Area")
    print("3. Calculate Volume")
    print("4. Calculate Base Area")
    print("5. Calculate Perimeter of Base")

    choice = input("Enter your choice (1-5): ")

    try:
        radius = float(input("Enter radius of hemisphere: "))

        if radius <= 0:
            print("Radius must be greater than zero.")
            return

        if choice == "1":
            result = 2 * math.pi * radius ** 2
            print("Curved Surface Area:", round(result, 2), "square units")

        elif choice == "2":
            result = 3 * math.pi * radius ** 2
            print("Total Surface Area:", round(result, 2), "square units")

        elif choice == "3":
            result = (2 / 3) * math.pi * radius ** 3
            print("Volume:", round(result, 2), "cubic units")

        elif choice == "4":
            result = math.pi * radius ** 2
            print("Base Area:", round(result, 2), "square units")

        elif choice == "5":
            result = 2 * math.pi * radius
            print("Perimeter of Base:", round(result, 2), "units")

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    except ValueError:
        print("Please enter a valid numeric radius.")

hemispheremeasurement()