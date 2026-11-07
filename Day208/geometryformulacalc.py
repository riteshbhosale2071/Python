import math

def geometryformulacalc():
    print("Geometry Formula Calculator")
    print("1. Square Area and Perimeter")
    print("2. Rectangle Area and Perimeter")
    print("3. Triangle Area")
    print("4. Circle Area and Circumference")
    print("5. Trapezium Area")
    print("6. Cube Volume and Surface Area")
    print("7. Cuboid Volume and Surface Area")
    print("8. Cylinder Volume and Surface Area")
    print("9. Cone Volume and Surface Area")
    print("10. Sphere Volume and Surface Area")

    choice = input("Enter your choice (1-10): ")

    try:
        if choice == "1":
            side = float(input("Enter side length: "))
            if side <= 0:
                print("Side length must be positive.")
                return

            area = side ** 2
            perimeter = 4 * side
            print("Area:", round(area, 2))
            print("Perimeter:", round(perimeter, 2))

        elif choice == "2":
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))

            if length <= 0 or breadth <= 0:
                print("Dimensions must be positive.")
                return

            area = length * breadth
            perimeter = 2 * (length + breadth)
            print("Area:", round(area, 2))
            print("Perimeter:", round(perimeter, 2))

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            if base <= 0 or height <= 0:
                print("Dimensions must be positive.")
                return

            area = 0.5 * base * height
            print("Triangle Area:", round(area, 2))

        elif choice == "4":
            radius = float(input("Enter radius: "))

            if radius <= 0:
                print("Radius must be positive.")
                return

            area = math.pi * radius ** 2
            circumference = 2 * math.pi * radius
            print("Circle Area:", round(area, 2))
            print("Circumference:", round(circumference, 2))

        elif choice == "5":
            a = float(input("Enter first parallel side: "))
            b = float(input("Enter second parallel side: "))
            height = float(input("Enter height: "))

            if a <= 0 or b <= 0 or height <= 0:
                print("Dimensions must be positive.")
                return

            area = 0.5 * (a + b) * height
            print("Trapezium Area:", round(area, 2))

        elif choice == "6":
            side = float(input("Enter cube side: "))

            if side <= 0:
                print("Side length must be positive.")
                return

            volume = side ** 3
            surface_area = 6 * side ** 2
            print("Volume:", round(volume, 2))
            print("Surface Area:", round(surface_area, 2))

        elif choice == "7":
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            h = float(input("Enter height: "))

            if l <= 0 or b <= 0 or h <= 0:
                print("Dimensions must be positive.")
                return

            volume = l * b * h
            surface_area = 2 * (l * b + b * h + h * l)
            print("Volume:", round(volume, 2))
            print("Surface Area:", round(surface_area, 2))

        elif choice == "8":
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))

            if r <= 0 or h <= 0:
                print("Dimensions must be positive.")
                return

            volume = math.pi * r ** 2 * h
            surface_area = 2 * math.pi * r * (r + h)
            print("Volume:", round(volume, 2))
            print("Total Surface Area:", round(surface_area, 2))

        elif choice == "9":
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))

            if r <= 0 or h <= 0:
                print("Dimensions must be positive.")
                return

            slant_height = math.sqrt(r ** 2 + h ** 2)
            volume = (math.pi * r ** 2 * h) / 3
            surface_area = math.pi * r * (r + slant_height)
            print("Volume:", round(volume, 2))
            print("Total Surface Area:", round(surface_area, 2))

        elif choice == "10":
            r = float(input("Enter radius: "))

            if r <= 0:
                print("Radius must be positive.")
                return

            volume = (4 / 3) * math.pi * r ** 3
            surface_area = 4 * math.pi * r ** 2
            print("Volume:", round(volume, 2))
            print("Surface Area:", round(surface_area, 2))

        else:
            print("Invalid choice. Please select from 1 to 10.")

    except ValueError:
        print("Please enter valid numeric values.")

geometryformulacalc()