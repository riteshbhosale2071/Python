import math

def trigonometricratiocalculator():
    angle = float(input("Enter the angle in degrees: "))

    radians = math.radians(angle)

    sin_value = math.sin(radians)
    cos_value = math.cos(radians)

    print(f"\nAngle: {angle:g} degrees")
    print(f"sin({angle:g}°) = {sin_value:.4f}")
    print(f"cos({angle:g}°) = {cos_value:.4f}")

    if math.isclose(cos_value, 0, abs_tol=1e-9):
        print("tan is undefined.")
    else:
        print(f"tan({angle:g}°) = {math.tan(radians):.4f}")

    if math.isclose(sin_value, 0, abs_tol=1e-9):
        print("cosec is undefined.")
    else:
        print(f"cosec({angle:g}°) = {1 / sin_value:.4f}")

    if math.isclose(cos_value, 0, abs_tol=1e-9):
        print("sec is undefined.")
    else:
        print(f"sec({angle:g}°) = {1 / cos_value:.4f}")

    if math.isclose(math.tan(radians), 0, abs_tol=1e-9):
        print("cot is undefined.")
    else:
        print(f"cot({angle:g}°) = {1 / math.tan(radians):.4f}")

trigonometricratiocalculator()