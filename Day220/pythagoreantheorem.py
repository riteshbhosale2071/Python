import math

def pythagoreantheorem():
    print("Pythagorean Theorem Calculator")
    print("1. Find Hypotenuse")
    print("2. Find First Side")
    print("3. Find Second Side")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        a = float(input("Enter first perpendicular side: "))
        b = float(input("Enter second perpendicular side: "))

        if a <= 0 or b <= 0:
            print("Side lengths must be positive.")
            return

        c = math.sqrt(a ** 2 + b ** 2)
        print("Hypotenuse =", round(c, 4))

    elif choice == "2":
        c = float(input("Enter hypotenuse: "))
        b = float(input("Enter known perpendicular side: "))

        if c <= 0 or b <= 0 or c <= b:
            print("Hypotenuse must be greater than the known side.")
            return

        a = math.sqrt(c ** 2 - b ** 2)
        print("Missing side =", round(a, 4))

    elif choice == "3":
        c = float(input("Enter hypotenuse: "))
        a = float(input("Enter known perpendicular side: "))

        if c <= 0 or a <= 0 or c <= a:
            print("Hypotenuse must be greater than the known side.")
            return

        b = math.sqrt(c ** 2 - a ** 2)
        print("Missing side =", round(b, 4))

    else:
        print("Invalid choice.")

pythagoreantheorem()