import math

def asaconstructionvalidator():
    side_a = float(input("Enter a side length: "))
    angle_a = float(input("Enter first angle in degrees: "))
    angle_b = float(input("Enter second angle in degrees: "))
    side_c = float(input("Enter another side length: "))

    if side_a <= 0 or side_c <= 0:
        print("Invalid side lengths. Both sides must be positive.")
        return

    if angle_a <= 0 or angle_b <= 0 or angle_a + angle_b >= 180:
        print("Invalid angles. Both must be positive and their sum must be less than 180 degrees.")
        return

    angle_c = 180 - angle_a - angle_b

    side_b = side_a * math.sin(math.radians(angle_b)) / math.sin(math.radians(angle_a))
    expected_side_c = side_a * math.sin(math.radians(angle_c)) / math.sin(math.radians(angle_a))

    if math.isclose(side_c, expected_side_c, rel_tol=1e-2):
        area = 0.5 * side_a * side_b * math.sin(math.radians(angle_c))
        perimeter = side_a + side_b + side_c

        print("Valid ASA triangle construction.")
        print(f"Third angle: {angle_c:.2f} degrees")
        print(f"Remaining side: {side_b:.2f}")
        print(f"Area: {area:.2f}")
        print(f"Perimeter: {perimeter:.2f}")
    else:
        print("Invalid ASA construction. The given side lengths and angles are inconsistent.")

asaconstructionvalidator()