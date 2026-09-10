def trianglecentrepropertychecker():
    print("Triangle Centre Property Checker :")

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

    print("\nTriangle Centre Properties :")
    print("Triangle Type:", triangle_type)
    print("Angle Type:", angle_type)

    print("\nCentroid:")
    print("Lies inside the triangle")
    print("Divides each median in the ratio 2:1")

    print("\nIncentre:")
    print("Lies inside the triangle")
    print("Is the intersection point of angle bisectors")

    print("\nCircumcentre:")
    if angle_type == "Acute-Angled":
        print("Lies inside the triangle")
    elif angle_type == "Right-Angled":
        print("Lies on the midpoint of the hypotenuse")
    else:
        print("Lies outside the triangle")

    print("\nOrthocentre:")
    if angle_type == "Acute-Angled":
        print("Lies inside the triangle")
    elif angle_type == "Right-Angled":
        print("Lies at the right-angled vertex")
    else:
        print("Lies outside the triangle")

    if triangle_type == "Equilateral":
        print("\nSpecial Property:")
        print("Centroid, Incentre, Circumcentre and Orthocentre are the same point.")

trianglecentrepropertychecker()