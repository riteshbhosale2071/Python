import math

def cylindersurfaceareacalculator():
    print("Cylinder Surface Area Calculator")
    print("1. Calculate Curved Surface Area")
    print("2. Calculate Total Surface Area")
    print("3. Calculate Base Area")
    print("4. Calculate Radius")
    print("5. Calculate Height")

    choice = input("Enter your choice (1-5): ")

    if choice in ("1", "2", "3"):
        radius = float(input("Enter cylinder radius: "))

        if radius <= 0:
            print("Radius must be positive.")
            return

        if choice in ("1", "2"):
            height = float(input("Enter cylinder height: "))
            if height <= 0:
                print("Height must be positive.")
                return

            if choice == "1":
                area = 2 * math.pi * radius * height
                label = "Curved Surface Area"
            else:
                area = 2 * math.pi * radius * (radius + height)
                label = "Total Surface Area"
        else:
            area = math.pi * radius ** 2
            label = "Base Area"

        print(label, "=", round(area, 2), "square units")

    elif choice == "4":
        area = float(input("Enter base area: "))
        if area <= 0:
            print("Area must be positive.")
            return
        radius = math.sqrt(area / math.pi)
        print("Radius =", round(radius, 2), "units")

    elif choice == "5":
        radius = float(input("Enter cylinder radius: "))
        csa = float(input("Enter curved surface area: "))

        if radius <= 0 or csa <= 0:
            print("Radius and area must be positive.")
            return

        height = csa / (2 * math.pi * radius)
        print("Height =", round(height, 2), "units")

    else:
        print("Invalid choice.")

cylindersurfaceareacalculator()