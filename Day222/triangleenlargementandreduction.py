def triangleenlargementandreduction():
    print("Triangle Enlargement and Reduction Calculator")

    a = float(input("Enter original side A: "))
    b = float(input("Enter original side B: "))
    c = float(input("Enter original side C: "))
    scale = float(input("Enter scale factor: "))

    if min(a, b, c, scale) <= 0:
        print("All values must be positive.")
        return

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle side lengths.")
        return

    if scale == 1:
        print("The triangle remains the same size.")
    elif scale > 1:
        print("Operation: Enlargement")
    else:
        print("Operation: Reduction")

    new_a = a * scale
    new_b = b * scale
    new_c = c * scale

    original_area_factor = 1
    new_area_factor = scale ** 2

    print("\nNew Triangle Side Lengths:")
    print("Side A =", round(new_a, 2))
    print("Side B =", round(new_b, 2))
    print("Side C =", round(new_c, 2))
    print("Length Scale Factor =", scale)
    print("Area Scale Factor =", round(new_area_factor, 4))
    print("Perimeter Scale Factor =", scale)

triangleenlargementandreduction()