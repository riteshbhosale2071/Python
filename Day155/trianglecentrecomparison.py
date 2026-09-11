def trianglecentrecomparison():
    print("Triangle Centre Comparison Engine :")

    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle.")
        return

    if a == b and b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    largest = a

    if b > largest:
        largest = b

    if c > largest:
        largest = c

    if largest == a:
        side1 = b
        side2 = c
    elif largest == b:
        side1 = a
        side2 = c
    else:
        side1 = a
        side2 = b

    if largest * largest == side1 * side1 + side2 * side2:
        angle_type = "Right-Angled"
    elif largest * largest < side1 * side1 + side2 * side2:
        angle_type = "Acute-Angled"
    else:
        angle_type = "Obtuse-Angled"

    print("\nComparison Engine Result :")
    print("Triangle Type:", triangle_type)
    print("Angle Type:", angle_type)

    print("\nCentre Comparison:")

    if triangle_type == "Equilateral":
        print("Centroid: Same point as all other centres")
        print("Incentre: Same point as all other centres")
        print("Circumcentre: Same point as all other centres")
        print("Orthocentre: Same point as all other centres")
        print("Result: All four centres coincide.")

    else:
        print("Centroid: Inside the triangle")
        print("Incentre: Inside the triangle")

        if angle_type == "Acute-Angled":
            print("Circumcentre: Inside the triangle")
            print("Orthocentre: Inside the triangle")
        elif angle_type == "Right-Angled":
            print("Circumcentre: On the midpoint of the hypotenuse")
            print("Orthocentre: At the right-angled vertex")
        else:
            print("Circumcentre: Outside the triangle")
            print("Orthocentre: Outside the triangle")

        print("\nResult: The four centres are distinct.")

        if triangle_type == "Isosceles":
            print("Special Property: The centres lie on the axis of symmetry.")

trianglecentrecomparison()