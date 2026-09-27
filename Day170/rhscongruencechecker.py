def rhscongruencechecker():
    print("RHS Congruence Checker :")

    print("\nEnter Triangle 1:")
    hypotenuse1 = float(input("Enter hypotenuse: "))
    side1 = float(input("Enter one corresponding side: "))

    print("\nEnter Triangle 2:")
    hypotenuse2 = float(input("Enter hypotenuse: "))
    side2 = float(input("Enter one corresponding side: "))

    if hypotenuse1 <= 0 or hypotenuse2 <= 0 or side1 <= 0 or side2 <= 0:
        print("Side lengths must be positive.")
        return

    if side1 >= hypotenuse1:
        print("Triangle 1 is invalid because the hypotenuse must be the longest side.")
        return

    if side2 >= hypotenuse2:
        print("Triangle 2 is invalid because the hypotenuse must be the longest side.")
        return

    if hypotenuse1 == hypotenuse2 and side1 == side2:
        print("\nResult: The triangles are congruent by RHS.")
        print("Both have equal hypotenuses and one equal corresponding side.")
    else:
        print("\nResult: The triangles are not proven congruent by RHS.")
        print("The required hypotenuse and corresponding side are not both equal.")

rhscongruencechecker()