import math

def radiusanddiameter():
    print("Radius and Diameter Converter")
    print("1. Convert radius to diameter")
    print("2. Convert diameter to radius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        radius = float(input("Enter the radius: "))

        if radius <= 0:
            print("Invalid radius. Radius must be positive.")
            return

        diameter = 2 * radius
        print(f"Radius: {radius:.2f}")
        print(f"Diameter: {diameter:.2f}")

    elif choice == "2":
        diameter = float(input("Enter the diameter: "))

        if diameter <= 0:
            print("Invalid diameter. Diameter must be positive.")
            return

        radius = diameter / 2
        print(f"Diameter: {diameter:.2f}")
        print(f"Radius: {radius:.2f}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

radiusanddiameter()