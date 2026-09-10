def trianglecentrecomparison():
    print("Triangle Centre Comparison :")

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

    other1 = a
    other2 = b

    if largest == a:
        other1 = b
        other2 = c
    elif largest == b:
        other1 = a
        other2 = c
    else:
        other1 = a
        other2 = b

    if largest * largest == other1 * other1 + other2 * other2:
        angle_type = "Right-Angled"
    elif largest * largest < other1 * other1 + other2 * other2:
        angle_type = "Acute-Angled"
    else:
        angle_type = "Obtuse-Angled"

    print("\nTriangle Centre Comparison :")
    print("Triangle Type:", triangle_type)
    print("Angle Type:", angle_type)

    if triangle_type == "Equilateral":
        print("Centroid = Incentre = Circumcentre = Orthocentre")
    elif angle_type == "Right-Angled":
        print("Orthocentre lies at the right-angled vertex")
        print("Circumcentre lies at the midpoint of the hypotenuse")
        print("Centroid and Incentre are different")
    elif angle_type == "Acute-Angled":
        print("All four centres lie inside the triangle")
        print("Centroid, Incentre, Circumcentre and Orthocentre are different")
    else:
        print("Orthocentre lies outside the triangle")
        print("Circumcentre lies outside the triangle")
        print("Centroid and Incentre lie inside the triangle")

trianglecentrecomparison()