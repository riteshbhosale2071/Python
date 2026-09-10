def orthocentretypeanalyzer():
    print("Orthocentre Type Analyzer :")

    a = float(input("Enter side AB: "))
    b = float(input("Enter side BC: "))
    c = float(input("Enter side CA: "))

    if a + b <= c or b + c <= a or a + c <= b:
        print("Invalid triangle.")
        return

    if a == b and b == c:
        print("Triangle Type: Equilateral")
        print("Orthocentre Type: Same as Centroid, Incentre and Circumcentre")

    elif a == b or b == c or a == c:
        print("Triangle Type: Isosceles")
        print("Orthocentre Type: Lies on the axis of symmetry")

    else:
        largest = a

        if b > largest:
            largest = b
        if c > largest:
            largest = c

        if largest * largest == a * a + b * b + c * c - largest * largest:
            print("Triangle Type: Right-Angled")
            print("Orthocentre Type: At the right-angled vertex")
        elif largest * largest < a * a + b * b + c * c - largest * largest:
            print("Triangle Type: Acute-Angled")
            print("Orthocentre Type: Inside the triangle")
        else:
            print("Triangle Type: Obtuse-Angled")
            print("Orthocentre Type: Outside the triangle")

orthocentretypeanalyzer()