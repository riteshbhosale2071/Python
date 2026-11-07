import math
import random


def getpositivenumber(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Enter a value greater than zero.")
        except ValueError:
            print("Enter a valid number.")


def getangle(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 < value < 180:
                return value
            print("Enter an angle between 0 and 180 degrees.")
        except ValueError:
            print("Enter a valid angle.")


def geometrycalculator():
    print("\nGEOMETRY CALCULATOR")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")

    choice = input("Choose a shape: ")

    if choice == "1":
        length = getpositivenumber("Enter length: ")
        width = getpositivenumber("Enter width: ")
        print("Area:", round(length * width, 2))
        print("Perimeter:", round(2 * (length + width), 2))

    elif choice == "2":
        side = getpositivenumber("Enter side: ")
        print("Area:", round(side ** 2, 2))
        print("Perimeter:", round(4 * side, 2))

    elif choice == "3":
        radius = getpositivenumber("Enter radius: ")
        print("Area:", round(math.pi * radius ** 2, 2))
        print("Circumference:", round(2 * math.pi * radius, 2))

    elif choice == "4":
        a = getpositivenumber("Enter first side: ")
        b = getpositivenumber("Enter second side: ")
        c = getpositivenumber("Enter third side: ")

        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print("Area:", round(area, 2))
            print("Perimeter:", round(a + b + c, 2))
        else:
            print("Invalid triangle sides.")

    else:
        print("Invalid choice.")


def parallellineanglecalculator():
    print("\nPARALLEL-LINE ANGLE CALCULATOR")
    angle = getangle("Enter one angle in degrees: ")

    print("1. Corresponding angle")
    print("2. Alternate interior angle")
    print("3. Alternate exterior angle")
    print("4. Co-interior angle")
    print("5. Vertically opposite angle")
    choice = input("Choose relationship: ")

    if choice in ["1", "2", "3", "5"]:
        result = angle
    elif choice == "4":
        result = 180 - angle
    else:
        print("Invalid choice.")
        return

    print("Required angle:", round(result, 2), "degrees")


def trianglecalculator():
    print("\nTRIANGLE CALCULATOR")
    print("1. Find third angle")
    print("2. Find area using base and height")
    print("3. Find hypotenuse")

    choice = input("Choose an operation: ")

    if choice == "1":
        a = getangle("Enter first angle: ")
        b = getangle("Enter second angle: ")

        if a + b < 180:
            print("Third angle:", 180 - a - b, "degrees")
        else:
            print("Invalid angles.")

    elif choice == "2":
        base = getpositivenumber("Enter base: ")
        height = getpositivenumber("Enter height: ")
        print("Triangle area:", round(0.5 * base * height, 2))

    elif choice == "3":
        a = getpositivenumber("Enter first perpendicular side: ")
        b = getpositivenumber("Enter second perpendicular side: ")
        print("Hypotenuse:", round(math.hypot(a, b), 2))

    else:
        print("Invalid choice.")


def constructioncalculator():
    print("\nGEOMETRICAL CONSTRUCTION ASSISTANT")
    print("1. Perpendicular bisector measurements")
    print("2. Circle construction measurements")
    print("3. Equilateral triangle height")

    choice = input("Choose a construction: ")

    if choice == "1":
        length = getpositivenumber("Enter line segment length: ")
        print("Midpoint distance from either end:", length / 2)

    elif choice == "2":
        radius = getpositivenumber("Enter circle radius: ")
        print("Compass opening:", radius)
        print("Diameter:", 2 * radius)
        print("Circumference:", round(2 * math.pi * radius, 2))

    elif choice == "3":
        side = getpositivenumber("Enter triangle side: ")
        height = math.sqrt(3) * side / 2
        print("Equilateral triangle height:", round(height, 2))

    else:
        print("Invalid choice.")


def quadrilateralcalculator():
    print("\nQUADRILATERAL CALCULATOR")
    print("1. Parallelogram")
    print("2. Trapezium")
    print("3. Rhombus")

    choice = input("Choose a quadrilateral: ")

    if choice == "1":
        base = getpositivenumber("Enter base: ")
        height = getpositivenumber("Enter height: ")
        side = getpositivenumber("Enter adjacent side: ")
        print("Area:", base * height)
        print("Perimeter:", 2 * (base + side))

    elif choice == "2":
        a = getpositivenumber("Enter first parallel side: ")
        b = getpositivenumber("Enter second parallel side: ")
        height = getpositivenumber("Enter height: ")
        print("Area:", round(0.5 * (a + b) * height, 2))

    elif choice == "3":
        side = getpositivenumber("Enter side length: ")
        d1 = getpositivenumber("Enter first diagonal: ")
        d2 = getpositivenumber("Enter second diagonal: ")

        if math.isclose(d1 ** 2 + d2 ** 2, 4 * side ** 2,
                        rel_tol=1e-5):
            print("Area:", round(0.5 * d1 * d2, 2))
            print("Perimeter:", 4 * side)
        else:
            print("Invalid rhombus measurements.")

    else:
        print("Invalid choice.")


def circlecalculator():
    print("\nCIRCLE CALCULATOR")
    radius = getpositivenumber("Enter radius: ")

    print("Diameter:", 2 * radius)
    print("Circumference:", round(2 * math.pi * radius, 2))
    print("Area:", round(math.pi * radius ** 2, 2))

    angle = getpositivenumber("Enter central angle in degrees: ")

    if angle <= 360:
        arc_length = (angle / 360) * 2 * math.pi * radius
        sector_area = (angle / 360) * math.pi * radius ** 2
        print("Arc length:", round(arc_length, 2))
        print("Sector area:", round(sector_area, 2))
    else:
        print("Central angle cannot exceed 360 degrees.")


def coordinategeometrycalculator():
    print("\nCOORDINATE GEOMETRY CALCULATOR")
    print("1. Distance between two points")
    print("2. Midpoint")
    print("3. Slope")
    print("4. Section midpoint")

    choice = input("Choose an operation: ")

    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        if choice == "1":
            distance = math.hypot(x2 - x1, y2 - y1)
            print("Distance:", round(distance, 2))

        elif choice == "2":
            print("Midpoint:", ((x1 + x2) / 2, (y1 + y2) / 2))

        elif choice == "3":
            if x2 == x1:
                print("Slope is undefined (vertical line).")
            else:
                print("Slope:", (y2 - y1) / (x2 - x1))

        elif choice == "4":
            print("Midpoint:", ((x1 + x2) / 2, (y1 + y2) / 2))

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid coordinates.")


def trigonometrycalculator():
    print("\nTRIGONOMETRY CALCULATOR")
    angle = getpositivenumber("Enter angle in degrees: ")

    if angle >= 360:
        print("Enter an angle less than 360 degrees.")
        return

    radians = math.radians(angle)

    print("Sine:", round(math.sin(radians), 4))
    print("Cosine:", round(math.cos(radians), 4))

    if not math.isclose(math.cos(radians), 0, abs_tol=1e-10):
        print("Tangent:", round(math.tan(radians), 4))
    else:
        print("Tangent: Undefined")

    print("Cosecant:",
          "Undefined" if math.isclose(math.sin(radians), 0, abs_tol=1e-10)
          else round(1 / math.sin(radians), 4))

    print("Secant:",
          "Undefined" if math.isclose(math.cos(radians), 0, abs_tol=1e-10)
          else round(1 / math.cos(radians), 4))


def surfaceareavolumecalculator():
    print("\nSURFACE AREA AND VOLUME")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")
    print("6. Hemisphere")

    choice = input("Choose a solid: ")

    if choice == "1":
        a = getpositivenumber("Enter side: ")
        print("Total surface area:", 6 * a ** 2)
        print("Volume:", a ** 3)

    elif choice == "2":
        l = getpositivenumber("Enter length: ")
        w = getpositivenumber("Enter width: ")
        h = getpositivenumber("Enter height: ")
        print("Total surface area:", 2 * (l * w + w * h + h * l))
        print("Volume:", l * w * h)

    elif choice == "3":
        r = getpositivenumber("Enter radius: ")
        h = getpositivenumber("Enter height: ")
        print("Curved surface area:", round(2 * math.pi * r * h, 2))
        print("Total surface area:", round(2 * math.pi * r * (r + h), 2))
        print("Volume:", round(math.pi * r ** 2 * h, 2))

    elif choice == "4":
        r = getpositivenumber("Enter radius: ")
        h = getpositivenumber("Enter height: ")
        slant = math.hypot(r, h)
        print("Slant height:", round(slant, 2))
        print("Curved surface area:", round(math.pi * r * slant, 2))
        print("Total surface area:", round(math.pi * r * (r + slant), 2))
        print("Volume:", round(math.pi * r ** 2 * h / 3, 2))

    elif choice == "5":
        r = getpositivenumber("Enter radius: ")
        print("Surface area:", round(4 * math.pi * r ** 2, 2))
        print("Volume:", round((4 / 3) * math.pi * r ** 3, 2))

    elif choice == "6":
        r = getpositivenumber("Enter radius: ")
        print("Curved surface area:", round(2 * math.pi * r ** 2, 2))
        print("Total surface area:", round(3 * math.pi * r ** 2, 2))
        print("Volume:", round((2 / 3) * math.pi * r ** 3, 2))

    else:
        print("Invalid choice.")


def mathematicsquiz():
    questions = [
        ("Sum of angles in a triangle?", "180"),
        ("How many sides does a hexagon have?", "6"),
        ("Area of a circle formula uses which constant?", "pi"),
        ("How many degrees are in a right angle?", "90"),
        ("How many diagonals does a rectangle have?", "2"),
        ("What is the square root of 144?", "12"),
        ("What is the sum of angles in a quadrilateral?", "360"),
        ("How many faces does a cube have?", "6")
    ]

    random.shuffle(questions)
    score = 0

    print("\nMATHEMATICS QUIZ")

    for number, (question, answer) in enumerate(questions, 1):
        print(f"\n{number}. {question}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Correct answer:", answer)

    percentage = score / len(questions) * 100

    print("\nQUIZ RESULT")
    print("Score:", score, "/", len(questions))
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        print("Performance: Excellent")
    elif percentage >= 60:
        print("Performance: Good")
    elif percentage >= 40:
        print("Performance: Average")
    else:
        print("Performance: Needs Improvement")


def completemathematicstoolkit():
    while True:
        print(" COMPLETE MATHEMATICS TOOLKIT")
        print("1. Geometry Calculator")
        print("2. Parallel-Line Angle Calculator")
        print("3. Triangle Calculator")
        print("4. Geometrical Construction Assistant")
        print("5. Quadrilateral Calculator")
        print("6. Circle Calculator")
        print("7. Coordinate Geometry Calculator")
        print("8. Trigonometry Calculator")
        print("9. Surface Area and Volume Calculator")
        print("10. Mathematics Quiz")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            geometrycalculator()
        elif choice == "2":
            parallellineanglecalculator()
        elif choice == "3":
            trianglecalculator()
        elif choice == "4":
            constructioncalculator()
        elif choice == "5":
            quadrilateralcalculator()
        elif choice == "6":
            circlecalculator()
        elif choice == "7":
            coordinategeometrycalculator()
        elif choice == "8":
            trigonometrycalculator()
        elif choice == "9":
            surfaceareavolumecalculator()
        elif choice == "10":
            mathematicsquiz()
        elif choice == "0":
            print("Thank you for using the Mathematics Toolkit!")
            break
        else:
            print("Invalid choice. Please select from 0 to 10.")

completemathematicstoolkit()