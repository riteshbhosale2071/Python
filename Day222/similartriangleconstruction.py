def similartriangleconstruction():
    print("Similar Triangle Construction Calculator")

    scale = float(input("Enter scale factor (new/original): "))
    side_a = float(input("Enter original side A: "))
    side_b = float(input("Enter original side B: "))
    side_c = float(input("Enter original side C: "))

    if scale <= 0 or min(side_a, side_b, side_c) <= 0:
        print("Scale factor and side lengths must be positive.")
        return

    if (side_a + side_b <= side_c or
            side_a + side_c <= side_b or
            side_b + side_c <= side_a):
        print("Invalid original triangle side lengths.")
        return

    new_a = side_a * scale
    new_b = side_b * scale
    new_c = side_c * scale

    print("\nConstructed Similar Triangle:")
    print("New Side A =", round(new_a, 2))
    print("New Side B =", round(new_b, 2))
    print("New Side C =", round(new_c, 2))
    print("Scale Factor =", scale)
    print("Area Scale Factor =", round(scale ** 2, 2))

    print("\nThe new triangle is similar to the original triangle.")

similartriangleconstruction()