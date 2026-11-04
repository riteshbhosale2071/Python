def sectionformulacalculator():
    x1 = float(input("Enter the X-coordinate of the first point: "))
    y1 = float(input("Enter the Y-coordinate of the first point: "))

    x2 = float(input("Enter the X-coordinate of the second point: "))
    y2 = float(input("Enter the Y-coordinate of the second point: "))

    m = float(input("Enter the ratio numerator (m): "))
    n = float(input("Enter the ratio denominator (n): "))

    if m < 0 or n < 0 or m + n == 0:
        print("Invalid ratio. Enter non-negative values whose sum is positive.")
        return

    section_x = (m * x2 + n * x1) / (m + n)
    section_y = (m * y2 + n * y1) / (m + n)

    print(f"First Point: ({x1:.2f}, {y1:.2f})")
    print(f"Second Point: ({x2:.2f}, {y2:.2f})")
    print(f"Ratio: {m:g}:{n:g}")
    print(f"Section Point: ({section_x:.2f}, {section_y:.2f})")

sectionformulacalculator()