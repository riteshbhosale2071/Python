def geometrypropertyvalidator():
    print("Geometry Property Validator :")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Circle")
    print("5. Cuboid")

    choice = int(input("Select a geometry type: "))

    if choice == 1:
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Sides must be greater than zero.")
            return

        if a + b > c and a + c > b and b + c > a:
            print("Property: Valid Triangle")
            perimeter = a + b + c
            print("Perimeter:", round(perimeter, 2))

            if a == b == c:
                print("Type: Equilateral Triangle")
            elif a == b or b == c or a == c:
                print("Type: Isosceles Triangle")
            else:
                print("Type: Scalene Triangle")
        else:
            print("Property: Invalid Triangle")

    elif choice == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        if length > 0 and width > 0:
            print("Property: Valid Rectangle")
            print("Area:", round(length * width, 2))
            print("Perimeter:", round(2 * (length + width), 2))
        else:
            print("Length and width must be greater than zero.")

    elif choice == 3:
        side = float(input("Enter side: "))

        if side > 0:
            print("Property: Valid Square")
            print("Area:", round(side ** 2, 2))
            print("Perimeter:", round(4 * side, 2))
        else:
            print("Side must be greater than zero.")

    elif choice == 4:
        radius = float(input("Enter radius: "))

        if radius > 0:
            pi = 3.14159
            print("Property: Valid Circle")
            print("Area:", round(pi * radius ** 2, 2))
            print("Circumference:", round(2 * pi * radius, 2))
        else:
            print("Radius must be greater than zero.")

    elif choice == 5:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))

        if length > 0 and width > 0 and height > 0:
            volume = length * width * height
            surface_area = 2 * (length * width + width * height + length * height)

            print("Property: Valid Cuboid")
            print("Volume:", round(volume, 2))
            print("Surface Area:", round(surface_area, 2))
        else:
            print("All dimensions must be greater than zero.")

    else:
        print("Invalid geometry selection.")

geometrypropertyvalidator()