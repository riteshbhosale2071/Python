import math

def circletangentconstruction():
    print("Circle Tangent Construction Assistant")
    print("1. Find Tangent Length")
    print("2. Find Tangent Point Distance")
    print("3. Verify Tangent Condition")
    print("4. Find Tangent Length from External Point")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter distance from center to external point: "))

        if radius <= 0 or distance <= radius:
            print("External point must be outside the circle.")
            return

        length = math.sqrt(distance ** 2 - radius ** 2)
        print("Tangent Length =", round(length, 2))

    elif choice == "2":
        distance = float(input("Enter distance from center to external point: "))
        tangent = float(input("Enter tangent length: "))

        if distance <= 0 or tangent < 0 or tangent >= distance:
            print("Invalid measurements.")
            return

        radius = math.sqrt(distance ** 2 - tangent ** 2)
        print("Circle Radius =", round(radius, 2))

    elif choice == "3":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter distance from center to external point: "))
        tangent = float(input("Enter perpendicular distance from center to tangent line: "))

        if radius <= 0 or distance <= 0 or tangent < 0:
            print("Measurements must be positive.")
            return

        if math.isclose(tangent, radius, rel_tol=1e-9, abs_tol=1e-9):
            print("Valid tangent: The line touches the circle at exactly one point.")
        else:
            print("Not a valid tangent line.")

    elif choice == "4":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter external point distance from center: "))

        if radius <= 0 or distance <= radius:
            print("External point must be outside the circle.")
            return

        tangent = math.sqrt(distance ** 2 - radius ** 2)
        print("Length of each tangent =", round(tangent, 2))
        print("Two equal tangents can be drawn from the external point.")

    else:
        print("Invalid choice.")

circletangentconstruction()