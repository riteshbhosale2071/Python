import math

def righttriangleside():
    print("Right Triangle Side Calculator")
    print("1. Calculate hypotenuse")
    print("2. Calculate missing side")

    choice = input("Enter your choice (1 or 2): ").strip()

    try:
        if choice == "1":
            side_a = float(input("Enter the first perpendicular side: "))
            side_b = float(input("Enter the second perpendicular side: "))

            if side_a <= 0 or side_b <= 0:
                print("Error: Side lengths must be greater than zero.")
                return

            hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)

            print("Hypotenuse:", round(hypotenuse, 2))

        elif choice == "2":
            hypotenuse = float(input("Enter the hypotenuse: "))
            known_side = float(input("Enter the known perpendicular side: "))

            if hypotenuse <= 0 or known_side <= 0:
                print("Error: Side lengths must be greater than zero.")
                return

            if known_side >= hypotenuse:
                print("Error: Hypotenuse must be longer than the known side.")
                return

            missing_side = math.sqrt(
                hypotenuse ** 2 - known_side ** 2
            )

            print("Missing side:", round(missing_side, 2))

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Error: Please enter numeric values.")

if __name__ == "__main__":
    righttriangleside()