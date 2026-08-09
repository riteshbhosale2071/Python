def perpendicularlines():
    print("Check Whether Two Lines Are Perpendicular")
    print("For two non-vertical lines, their slopes must be negative reciprocals.")

    m1 = float(input("Enter slope of Line 1: "))
    m2 = float(input("Enter slope of Line 2: "))

    if m1 == 0 and m2 != 0:
        print("The lines are perpendicular.")
    elif m2 == 0 and m1 != 0:
        print("The lines are perpendicular.")
    elif m1 * m2 == -1:
        print("The lines are perpendicular.")
    else:
        print("The lines are not perpendicular.")

perpendicularlines()