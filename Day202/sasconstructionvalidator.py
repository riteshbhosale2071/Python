import math

def sasconstructionvalidator():
    side_a = float(input("Enter first side length: "))
    side_b = float(input("Enter second side length: "))
    angle = float(input("Enter included angle in degrees: "))

    if side_a <= 0 or side_b <= 0:
        print("Invalid side lengths. Both sides must be positive.")
        return

    if angle <= 0 or angle >= 180:
        print("Invalid angle. The included angle must be between 0 and 180 degrees.")
        return

    angle_radians = math.radians(angle)
    side_c = math.sqrt(
        side_a**2 + side_b**2
        - 2 * side_a * side_b * math.cos(angle_radians)
    )

    area = 0.5 * side_a * side_b * math.sin(angle_radians)
    perimeter = side_a + side_b + side_c

    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        print("Valid SAS triangle construction.")
        print(f"Third side: {side_c:.2f}")
        print(f"Area: {area:.2f}")
        print(f"Perimeter: {perimeter:.2f}")
    else:
        print("Invalid SAS triangle construction.")

sasconstructionvalidator()