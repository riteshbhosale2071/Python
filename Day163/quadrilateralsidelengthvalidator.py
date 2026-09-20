def quadrilateralsidelengthvalidator():
    print("Quadrilateral Side-Length Validator :")

    side1 = float(input("Enter length of side 1: "))
    side2 = float(input("Enter length of side 2: "))
    side3 = float(input("Enter length of side 3: "))
    side4 = float(input("Enter length of side 4: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0 or side4 <= 0:
        print("Invalid quadrilateral.")
        print("All side lengths must be greater than zero.")
    elif side1 + side2 + side3 > side4 and side1 + side2 + side4 > side3 and side1 + side3 + side4 > side2 and side2 + side3 + side4 > side1:
        print("The given side lengths can form a quadrilateral.")

        if side1 == side2 == side3 == side4:
            print("All four sides are equal.")
            print("The quadrilateral may be a rhombus or square.")
        elif side1 == side3 and side2 == side4:
            print("Opposite sides are equal.")
            print("The quadrilateral may be a parallelogram or rectangle.")
        elif side1 == side2 and side3 == side4:
            print("Two pairs of adjacent sides are equal.")
            print("The quadrilateral may be a kite.")
        else:
            print("The quadrilateral has unequal side lengths.")
    else:
        print("The given side lengths cannot form a quadrilateral.")

quadrilateralsidelengthvalidator()