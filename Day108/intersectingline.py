def intersectingline():
    slope1 = float(input("Enter slope of first line: "))
    slope2 = float(input("Enter slope of second line: "))

    if slope1 != slope2:
        print("The lines are Intersecting")
    else:
        print("The lines are Parallel")

intersectingline()