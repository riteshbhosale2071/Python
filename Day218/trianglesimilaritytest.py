import math

def trianglesimilaritytest():
    print("Triangle Similarity Test Analyzer")

    print("\nEnter the sides of Triangle 1:")
    a1 = float(input("Enter side 1: "))
    b1 = float(input("Enter side 2: "))
    c1 = float(input("Enter side 3: "))

    print("\nEnter the sides of Triangle 2:")
    a2 = float(input("Enter side 1: "))
    b2 = float(input("Enter side 2: "))
    c2 = float(input("Enter side 3: "))

    if min(a1, b1, c1, a2, b2, c2) <= 0:
        print("All side lengths must be positive.")
        return

    if (a1 + b1 <= c1 or a1 + c1 <= b1 or b1 + c1 <= a1 or
        a2 + b2 <= c2 or a2 + c2 <= b2 or b2 + c2 <= a2):
        print("Invalid triangle: Triangle inequality is not satisfied.")
        return

    triangle1 = sorted([a1, b1, c1])
    triangle2 = sorted([a2, b2, c2])

    ratios = [triangle1[i] / triangle2[i] for i in range(3)]

    print("\nSSS Similarity Test:")
    print("Side ratios:", [round(r, 4) for r in ratios])

    if math.isclose(ratios[0], ratios[1], rel_tol=1e-9) and math.isclose(ratios[1], ratios[2], rel_tol=1e-9):
        print("Result: Both triangles are similar.")
        print("Similarity criterion: SSS (Side-Side-Side).")
        print("Scale factor:", round(ratios[0], 4))
    else:
        print("Result: Both triangles are not similar.")
        print("Corresponding sides are not proportional.")

trianglesimilaritytest()