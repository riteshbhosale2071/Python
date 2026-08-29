import math

def anglebisectorverification():
    print("Enter the two angles formed by the proposed angle bisector.")

    angle1 = float(input("Enter first angle: "))
    angle2 = float(input("Enter second angle: "))

    if angle1 <= 0 or angle2 <= 0:
        print("Angles must be positive.")
        return

    print("First Angle:", angle1, "°")
    print("Second Angle:", angle2, "°")

    if math.isclose(angle1, angle2, rel_tol=1e-9):
        print("Valid Angle Bisector.")
        print("The angle is divided into two equal angles.")
    else:
        print("Not an Angle Bisector.")
        print("The two angles are not equal.")

anglebisectorverification()