import math

def trianglearearatiocalculator():
    print("Triangle Area Ratio Calculator")

    print("\nEnter sides of first triangle:")
    a1 = float(input("Enter first side: "))
    b1 = float(input("Enter second side: "))
    c1 = float(input("Enter third side: "))

    print("\nEnter sides of second triangle:")
    a2 = float(input("Enter first side: "))
    b2 = float(input("Enter second side: "))
    c2 = float(input("Enter third side: "))

    if min(a1, b1, c1, a2, b2, c2) <= 0:
        print("Side lengths must be positive.")
        return

    if a1 + b1 <= c1 or a1 + c1 <= b1 or b1 + c1 <= a1:
        print("First triangle is invalid.")
        return

    if a2 + b2 <= c2 or a2 + c2 <= b2 or b2 + c2 <= a2:
        print("Second triangle is invalid.")
        return

    sides1 = sorted([a1, b1, c1])
    sides2 = sorted([a2, b2, c2])

    ratio1 = sides2[0] / sides1[0]
    ratio2 = sides2[1] / sides1[1]
    ratio3 = sides2[2] / sides1[2]

    if not (math.isclose(ratio1, ratio2, rel_tol=1e-9) and math.isclose(ratio2, ratio3, rel_tol=1e-9)):
        print("Triangles are not similar.")
        print("Area ratio cannot be determined using corresponding side ratios.")
        return

    side_ratio = ratio1
    area_ratio = side_ratio ** 2

    print("\nTriangle Area Ratio Result:")
    print("Side Ratio:", round(side_ratio, 2))
    print("Area Ratio:", round(area_ratio, 2))
    print("Area Ratio (First : Second):", f"1 : {area_ratio:.2f}")

trianglearearatiocalculator()