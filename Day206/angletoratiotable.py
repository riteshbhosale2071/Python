import math

def angletoratiotable():
    print("Angle-to-Ratio Table Generator")

    try:
        start_angle = int(input("Enter starting angle (degrees): "))
        end_angle = int(input("Enter ending angle (degrees): "))
        step = int(input("Enter angle step: "))

        if step <= 0:
            print("Step must be greater than zero.")
            return

        if start_angle > end_angle:
            print("Starting angle must not be greater than ending angle.")
            return

        print("\nAngle\tSin\t\tCos\t\tTan")

        for angle in range(start_angle, end_angle + 1, step):
            radians = math.radians(angle)

            sin_value = math.sin(radians)
            cos_value = math.cos(radians)

            if math.isclose(cos_value, 0, abs_tol=1e-10):
                tan_value = "Undefined"
            else:
                tan_value = f"{math.tan(radians):.4f}"

            print(
                f"{angle}°\t"
                f"{sin_value:.4f}\t\t"
                f"{cos_value:.4f}\t\t"
                f"{tan_value}"
            )

    except ValueError:
        print("Please enter valid integer values.")

angletoratiotable()