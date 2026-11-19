def similartriangleareacalcu():
    print("Similar Triangle Area Calculator")

    area1 = float(input("Enter the area of the first triangle: "))
    side1 = float(input("Enter a corresponding side of the first triangle: "))
    side2 = float(input("Enter the corresponding side of the second triangle: "))

    if area1 <= 0 or side1 <= 0 or side2 <= 0:
        print("All values must be positive.")
        return

    ratio = side2 / side1
    area2 = area1 * ratio ** 2

    print("\nSimilar Triangle Area Calculation:")
    print("Side ratio =", round(ratio, 4))
    print("Area ratio =", round(ratio ** 2, 4))
    print("Area of first triangle =", area1)
    print("Area of second triangle =", round(area2, 4))

similartriangleareacalcu()