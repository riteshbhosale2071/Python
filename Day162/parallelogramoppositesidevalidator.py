def parallelogramoppositesidevalidator():
    print("Parallelogram Opposite-Side Validator :")

    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter opposite side of first side: "))
    side4 = float(input("Enter opposite side of second side: "))

    if side1 == side3 and side2 == side4:
        print("The opposite sides are equal.")
        print("The sides satisfy the parallelogram property.")
    else:
        print("The opposite sides are not equal.")
        print("The sides do not satisfy the parallelogram property.")

parallelogramoppositesidevalidator()