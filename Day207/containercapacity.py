import math

def containercapacity():
    print("Container Capacity Calculator")
    print("1. Cylindrical Container")
    print("2. Cuboid Container")
    print("3. Cubical Container")
    print("4. Conical Container")
    print("5. Spherical Container")

    choice = input("Select container type (1-5): ")

    try:
        if choice == "1":
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))

            if radius <= 0 or height <= 0:
                print("Dimensions must be greater than zero.")
                return

            capacity = math.pi * radius ** 2 * height

        elif choice == "2":
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            height = float(input("Enter height: "))

            if length <= 0 or breadth <= 0 or height <= 0:
                print("Dimensions must be greater than zero.")
                return

            capacity = length * breadth * height

        elif choice == "3":
            side = float(input("Enter side length: "))

            if side <= 0:
                print("Side length must be greater than zero.")
                return

            capacity = side ** 3

        elif choice == "4":
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))

            if radius <= 0 or height <= 0:
                print("Dimensions must be greater than zero.")
                return

            capacity = (math.pi * radius ** 2 * height) / 3

        elif choice == "5":
            radius = float(input("Enter radius: "))

            if radius <= 0:
                print("Radius must be greater than zero.")
                return

            capacity = (4 / 3) * math.pi * radius ** 3

        else:
            print("Invalid choice. Please select from 1 to 5.")
            return

        print("\nContainer Capacity:", round(capacity, 2), "cubic units")
        print("Capacity in litres:", round(capacity / 1000, 2), "litres")

    except ValueError:
        print("Please enter valid numeric dimensions.")

containercapacity()