import math

def righttrianglesimilarityanalyzer():
    print("Right Triangle Similarity Analyzer")

    print("\nEnter the sides of the first right triangle:")
    a1 = float(input("Enter first perpendicular side: "))
    b1 = float(input("Enter second perpendicular side: "))
    c1 = float(input("Enter hypotenuse: "))

    print("\nEnter the sides of the second right triangle:")
    a2 = float(input("Enter first perpendicular side: "))
    b2 = float(input("Enter second perpendicular side: "))
    c2 = float(input("Enter hypotenuse: "))

    if min(a1, b1, c1, a2, b2, c2) <= 0:
        print("All side lengths must be positive.")
        return

    if not math.isclose(a1**2 + b1**2, c1**2, rel_tol=1e-9):
        print("First triangle is not right-angled.")
        return

    if not math.isclose(a2**2 + b2**2, c2**2, rel_tol=1e-9):
        print("Second triangle is not right-angled.")
        return

    ratios = [a1 / a2, b1 / b2, c1 / c2]

    print("\nCorresponding Side Ratios:")
    print("First ratio =", round(ratios[0], 4))
    print("Second ratio =", round(ratios[1], 4))
    print("Hypotenuse ratio =", round(ratios[2], 4))

    if all(math.isclose(ratios[0], r, rel_tol=1e-9) for r in ratios[1:]):
        print("\nResult: The right triangles are similar.")
        print("Similarity criterion: AA (Angle-Angle).")
        print("Scale factor =", round(ratios[0], 4))
    else:
        print("\nResult: The right triangles are not similar.")
        print("Their corresponding side ratios are not equal.")

righttrianglesimilarityanalyzer()