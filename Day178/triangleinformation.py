def triangleinformation():
    print("Triangle Information :")
    print("1. Three Sides")
    print("2. Base and Height")
    print("3. Two Sides and Included Angle")

    choice = int(input("Select information type: "))

    if choice == 1:
        a = float(input("Enter side A: "))
        b = float(input("Enter side B: "))
        c = float(input("Enter side C: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Sides must be greater than zero.")
            return

        if a + b <= c or a + c <= b or b + c <= a:
            print("The given sides cannot form a triangle.")
            return

        perimeter = a + b + c
        semi_perimeter = perimeter / 2
        area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5

        print("\nTriangle Information :")
        print("Perimeter:", round(perimeter, 2))
        print("Semi-Perimeter:", round(semi_perimeter, 2))
        print("Area:", round(area, 2))

        if a == b == c:
            print("Type: Equilateral")
        elif a == b or b == c or a == c:
            print("Type: Isosceles")
        else:
            print("Type: Scalene")

    elif choice == 2:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))

        if base <= 0 or height <= 0:
            print("Base and height must be greater than zero.")
            return

        area = 0.5 * base * height

        print("\nTriangle Information :")
        print("Base:", base)
        print("Height:", height)
        print("Area:", round(area, 2))

    elif choice == 3:
        side_a = float(input("Enter first side: "))
        side_b = float(input("Enter second side: "))
        angle = float(input("Enter included angle in degrees: "))

        if side_a <= 0 or side_b <= 0:
            print("Sides must be greater than zero.")
            return

        if angle <= 0 or angle >= 180:
            print("Angle must be between 0 and 180 degrees.")
            return

        print("\nTriangle Information :")
        print("Side A:", side_a)
        print("Side B:", side_b)
        print("Included Angle:", angle, "degrees")
        print("Area calculation requires the sine of the included angle.")

        print("Area Formula: 1/2 × A × B × sin(angle)")

    else:
        print("Invalid choice.")

triangleinformation()