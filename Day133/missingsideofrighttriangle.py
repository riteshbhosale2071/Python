import math

def missingsideofrighttriangle():
    choice = input("Find missing side (base/height/hypotenuse): ").lower()

    if choice == "hypotenuse":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))

        if base <= 0 or height <= 0:
            print("Sides must be positive.")
            return

        missing_side = math.sqrt(base ** 2 + height ** 2)
        print("Missing Hypotenuse:", missing_side)

    elif choice == "base":
        height = float(input("Enter height: "))
        hypotenuse = float(input("Enter hypotenuse: "))

        if height <= 0 or hypotenuse <= 0 or hypotenuse <= height:
            print("Invalid values.")
            return

        missing_side = math.sqrt(hypotenuse ** 2 - height ** 2)
        print("Missing Base:", missing_side)

    elif choice == "height":
        base = float(input("Enter base: "))
        hypotenuse = float(input("Enter hypotenuse: "))

        if base <= 0 or hypotenuse <= 0 or hypotenuse <= base:
            print("Invalid values.")
            return

        missing_side = math.sqrt(hypotenuse ** 2 - base ** 2)
        print("Missing Height:", missing_side)

    else:
        print("Invalid choice.")

missingsideofrighttriangle()