import math

def missingtrianglesidefinder():
    print("Missing Triangle Side Finder Using Trigonometry")
    print("1. Find Opposite Side")
    print("2. Find Adjacent Side")
    print("3. Find Hypotenuse")
    print("4. Find Missing Side Using Pythagorean Theorem")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        angle = float(input("Enter angle in degrees: "))
        hypotenuse = float(input("Enter hypotenuse: "))

        if not 0 < angle < 90 or hypotenuse <= 0:
            print("Enter a valid acute angle and positive hypotenuse.")
            return

        opposite = hypotenuse * math.sin(math.radians(angle))
        print("Opposite Side =", round(opposite, 2))

    elif choice == "2":
        angle = float(input("Enter angle in degrees: "))
        hypotenuse = float(input("Enter hypotenuse: "))

        if not 0 < angle < 90 or hypotenuse <= 0:
            print("Enter a valid acute angle and positive hypotenuse.")
            return

        adjacent = hypotenuse * math.cos(math.radians(angle))
        print("Adjacent Side =", round(adjacent, 2))

    elif choice == "3":
        angle = float(input("Enter angle in degrees: "))
        opposite = float(input("Enter opposite side: "))
        adjacent = float(input("Enter adjacent side: "))

        if not 0 < angle < 90 or min(opposite, adjacent) <= 0:
            print("Enter valid positive measurements and an acute angle.")
            return

        sine = math.sin(math.radians(angle))
        cosine = math.cos(math.radians(angle))

        if not math.isclose(opposite / adjacent, sine / cosine, rel_tol=1e-6):
            print("The given measurements are inconsistent.")
            return

        hypotenuse = math.hypot(opposite, adjacent)
        print("Hypotenuse =", round(hypotenuse, 2))

    elif choice == "4":
        print("1. Find Hypotenuse")
        print("2. Find Missing Leg")
        option = input("Enter your choice (1-2): ")

        if option == "1":
            a = float(input("Enter first leg: "))
            b = float(input("Enter second leg: "))

            if min(a, b) <= 0:
                print("Side lengths must be positive.")
                return

            print("Hypotenuse =", round(math.hypot(a, b), 2))

        elif option == "2":
            hypotenuse = float(input("Enter hypotenuse: "))
            side = float(input("Enter known leg: "))

            if hypotenuse <= 0 or side <= 0 or side >= hypotenuse:
                print("Invalid measurements.")
                return

            missing = math.sqrt(hypotenuse ** 2 - side ** 2)
            print("Missing Side =", round(missing, 2))

        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")

missingtrianglesidefinder()