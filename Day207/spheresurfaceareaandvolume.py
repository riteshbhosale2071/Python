import math

def spheresurfaceareaandvolume():
    print("Sphere Surface Area and Volume Calculator")
    print("1. Calculate Surface Area")
    print("2. Calculate Volume")
    print("3. Calculate Both")

    choice = input("Enter your choice (1-3): ")

    try:
        radius = float(input("Enter radius of sphere: "))

        if radius <= 0:
            print("Radius must be greater than zero.")
            return

        surface_area = 4 * math.pi * radius ** 2
        volume = (4 / 3) * math.pi * radius ** 3

        if choice == "1":
            print("Surface Area:", round(surface_area, 2), "square units")

        elif choice == "2":
            print("Volume:", round(volume, 2), "cubic units")

        elif choice == "3":
            print("Surface Area:", round(surface_area, 2), "square units")
            print("Volume:", round(volume, 2), "cubic units")

        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

    except ValueError:
        print("Please enter a valid numeric radius.")

spheresurfaceareaandvolume()