import math

def standardangletrigonometry():
    print("Standard Angle Trigonometry Calculator")
    print("1. 0 Degrees")
    print("2. 30 Degrees")
    print("3. 45 Degrees")
    print("4. 60 Degrees")
    print("5. 90 Degrees")
    print("6. Enter Custom Standard Angle")

    choice = input("Enter your choice (1-6): ")

    angles = {
        "1": 0,
        "2": 30,
        "3": 45,
        "4": 60,
        "5": 90
    }

    if choice in angles:
        angle = angles[choice]
    elif choice == "6":
        angle = float(input("Enter angle in degrees: "))
    else:
        print("Invalid choice.")
        return

    radian = math.radians(angle)
    sine = math.sin(radian)
    cosine = math.cos(radian)

    def formatvalue(value):
        if math.isclose(value, 0, abs_tol=1e-10):
            return "0"
        if math.isclose(value, 1, abs_tol=1e-10):
            return "1"
        if math.isclose(value, -1, abs_tol=1e-10):
            return "-1"
        return str(round(value, 4))

    print("\nAngle =", angle, "degrees")
    print("sin =", formatvalue(sine))
    print("cos =", formatvalue(cosine))
    print("tan =", "Undefined" if math.isclose(cosine, 0, abs_tol=1e-10) else formatvalue(sine / cosine))
    print("cosec =", "Undefined" if math.isclose(sine, 0, abs_tol=1e-10) else formatvalue(1 / sine))
    print("sec =", "Undefined" if math.isclose(cosine, 0, abs_tol=1e-10) else formatvalue(1 / cosine))
    print("cot =", "Undefined" if math.isclose(sine, 0, abs_tol=1e-10) else formatvalue(cosine / sine))

standardangletrigonometry()