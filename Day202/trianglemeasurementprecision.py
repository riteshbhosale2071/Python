def trianglemeasurementprecision():
    try:
        a = float(input("Enter first side length: "))
        b = float(input("Enter second side length: "))
        c = float(input("Enter third side length: "))
        precision = int(input("Enter decimal precision (0-10): "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Error: Side lengths must be positive.")
            return

        if a + b <= c or a + c <= b or b + c <= a:
            print("Error: These side lengths cannot form a triangle.")
            return

        if precision < 0 or precision > 10:
            print("Error: Precision must be between 0 and 10.")
            return

        perimeter = a + b + c
        semi_perimeter = perimeter / 2
        area = (
            semi_perimeter
            * (semi_perimeter - a)
            * (semi_perimeter - b)
            * (semi_perimeter - c)
        ) ** 0.5

        angle_a = round(
            __import__("math").degrees(
                __import__("math").acos(
                    (b**2 + c**2 - a**2) / (2 * b * c)
                )
            ),
            precision
        )

        angle_b = round(
            __import__("math").degrees(
                __import__("math").acos(
                    (a**2 + c**2 - b**2) / (2 * a * c)
                )
            ),
            precision
        )

        angle_c = round(180 - angle_a - angle_b, precision)

        print("\nTriangle Measurement Report")
        print(f"Side A: {a:.{precision}f}")
        print(f"Side B: {b:.{precision}f}")
        print(f"Side C: {c:.{precision}f}")
        print(f"Perimeter: {perimeter:.{precision}f}")
        print(f"Area: {area:.{precision}f}")
        print(f"Angle A: {angle_a:.{precision}f} degrees")
        print(f"Angle B: {angle_b:.{precision}f} degrees")
        print(f"Angle C: {angle_c:.{precision}f} degrees")

    except ValueError:
        print("Error: Enter valid numeric values.")

trianglemeasurementprecision()