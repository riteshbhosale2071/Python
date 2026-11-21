import math

def apolloniustheoremcalculator():
    print("Apollonius Theorem Calculator")
    print("Formula: AB² + AC² = 2(AD² + BD²)")
    print("Here, D is the midpoint of BC.")

    ab = float(input("Enter side AB: "))
    ac = float(input("Enter side AC: "))
    bc = float(input("Enter side BC: "))

    if min(ab, ac, bc) <= 0:
        print("All side lengths must be positive.")
        return

    if ab + ac <= bc or ab + bc <= ac or ac + bc <= ab:
        print("Invalid triangle: Triangle inequality is not satisfied.")
        return

    median = math.sqrt((2 * ab**2 + 2 * ac**2 - bc**2) / 4)

    print("\nApollonius Theorem Result:")
    print("Median AD =", round(median, 4))
    print("BD = DC =", round(bc / 2, 4))

    left = ab**2 + ac**2
    right = 2 * (median**2 + (bc / 2)**2)

    print("\nVerification:")
    print("AB² + AC² =", round(left, 4))
    print("2(AD² + BD²) =", round(right, 4))

    if math.isclose(left, right, rel_tol=1e-9):
        print("Apollonius Theorem is verified.")

apolloniustheoremcalculator()