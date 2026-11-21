import math

def missinghypotenusesegment():
    print("Missing Hypotenuse Segment Finder")
    print("Using the altitude theorem: h² = p × q")

    h = float(input("Enter the altitude to the hypotenuse: "))
    p = float(input("Enter the known hypotenuse segment: "))

    if h <= 0 or p <= 0:
        print("All values must be positive.")
        return

    q = (h ** 2) / p

    print("\nMissing Hypotenuse Segment =", round(q, 4))
    print("Total Hypotenuse Length =", round(p + q, 4))

    print("\nVerification:")
    print("Altitude squared =", round(h ** 2, 4))
    print("Product of segments =", round(p * q, 4))

    if math.isclose(h ** 2, p * q, rel_tol=1e-9):
        print("Result: The altitude theorem is verified.")

missinghypotenusesegment()