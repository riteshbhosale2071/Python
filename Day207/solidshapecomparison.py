import math

def solidshapecomparison():
    print("Solid Shape Comparison Tool")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")
    print("6. Hemisphere")

    try:
        choice = input("Select a solid shape (1-6): ")

        if choice == "1":
            side = float(input("Enter side length: "))
            if side <= 0:
                print("Dimensions must be greater than zero.")
                return

            volume = side ** 3
            surface_area = 6 * side ** 2

        elif choice == "2":
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            height = float(input("Enter height: "))

            if length <= 0 or breadth <= 0 or height <= 0:
                print("Dimensions must be greater than zero.")
                return

            volume = length * breadth * height
            surface_area = 2 * (
                length * breadth + breadth * height + height * length
            )

        elif choice == "3":
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))

            if radius <= 0 or height <= 0:
                print("Dimensions must be greater than zero.")
                return

            volume = math.pi * radius ** 2 * height
            surface_area = 2 * math.pi * radius * (radius + height)

        elif choice == "4":
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))

            if radius <= 0 or height <= 0:
                print("Dimensions must be greater than zero.")
                return

            slant_height = math.sqrt(radius ** 2 + height ** 2)
            volume = (math.pi * radius ** 2 * height) / 3
            surface_area = math.pi * radius * (radius + slant_height)

        elif choice == "5":
            radius = float(input("Enter radius: "))

            if radius <= 0:
                print("Radius must be greater than zero.")
                return

            volume = (4 / 3) * math.pi * radius ** 3
            surface_area = 4 * math.pi * radius ** 2

        elif choice == "6":
            radius = float(input("Enter radius: "))

            if radius <= 0:
                print("Radius must be greater than zero.")
                return

            volume = (2 / 3) * math.pi * radius ** 3
            surface_area = 3 * math.pi * radius ** 2

        else:
            print("Invalid choice. Please select a shape from 1 to 6.")
            return

        print("\nSolid Shape Measurements")
        print("Volume:", round(volume, 2), "cubic units")
        print("Total Surface Area:", round(surface_area, 2), "square units")

    except ValueError:
        print("Please enter valid numeric dimensions.")

solidshapecomparison()