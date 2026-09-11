def trianglecentreconsistency():
    print("Triangle Centre Consistency Checker :")

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

    print("\nConsistency Check :")
    print("Triangle Type:", triangle_type)
    print("Angle Type:", angle_type)

    if triangle_type == "Equilateral":
        print("Centroid = Incentre = Circumcentre = Orthocentre")
        print("All four centres are consistent at the same point.")

    elif angle_type == "Right-Angled":
        print("Centroid, Incentre, Circumcentre and Orthocentre are distinct.")
        print("Orthocentre is at the right-angled vertex.")
        print("Circumcentre is at the midpoint of the hypotenuse.")

    elif angle_type == "Acute-Angled":
        print("All four centres lie inside the triangle.")
        print("The centres are distinct unless the triangle is equilateral.")

    else:
        print("Centroid and Incentre lie inside the triangle.")
        print("Circumcentre and Orthocentre lie outside the triangle.")
        print("The centre positions are consistent with an obtuse triangle.")

trianglecentreconsistency()