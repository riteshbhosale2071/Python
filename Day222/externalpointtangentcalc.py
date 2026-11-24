import math

def externalpointtangentcalc():
    print("External Point Tangent Calculator")
    print("1. Calculate Tangent Length")
    print("2. Calculate Circle Radius")
    print("3. Calculate Distance from Center")
    print("4. Verify Tangent Measurements")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter distance from center to external point: "))

        if radius <= 0 or distance <= radius:
            print("Invalid measurements. External point must be outside the circle.")
            return

        tangent = math.sqrt(distance ** 2 - radius ** 2)
        print("Tangent Length =", round(tangent, 2))
        print("Both tangents from the external point have equal lengths.")

    elif choice == "2":
        distance = float(input("Enter distance from center to external point: "))
        tangent = float(input("Enter tangent length: "))

        if distance <= 0 or tangent <= 0 or tangent >= distance:
            print("Invalid measurements.")
            return

        radius = math.sqrt(distance ** 2 - tangent ** 2)
        print("Circle Radius =", round(radius, 2))

    elif choice == "3":
        radius = float(input("Enter circle radius: "))
        tangent = float(input("Enter tangent length: "))

        if radius <= 0 or tangent <= 0:
            print("Measurements must be positive.")
            return

        distance = math.sqrt(radius ** 2 + tangent ** 2)
        print("Distance from Center =", round(distance, 2))

    elif choice == "4":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter center-to-external-point distance: "))
        tangent = float(input("Enter measured tangent length: "))

        if radius <= 0 or distance <= 0 or tangent <= 0:
            print("Measurements must be positive.")
            return

        if distance <= radius:
            print("The point is not outside the circle.")
            return

        expected = math.sqrt(distance ** 2 - radius ** 2)

        if math.isclose(tangent, expected, rel_tol=1e-9, abs_tol=1e-9):
            print("Valid tangent measurements.")
        else:
            print("Invalid tangent measurements.")
            print("Expected Tangent Length =", round(expected, 2))

    else:
        print("Invalid choice.")

externalpointtangentcalc()