def insufficientdatadetector():
    print("Insufficient Data Detector :")

    print("\nEnter the available triangle evidence:")

    sides_equal = int(input("Enter number of corresponding equal side pairs: "))
    angles_equal = int(input("Enter number of corresponding equal angle pairs: "))

    right_triangle = input("Are both triangles right triangles? (yes/no): ").lower()

    if sides_equal < 0 or sides_equal > 3:
        print("Number of equal side pairs must be between 0 and 3.")
        return

    if angles_equal < 0 or angles_equal > 3:
        print("Number of equal angle pairs must be between 0 and 3.")
        return

    print("\nEvidence Check :")
    print("Equal Side Pairs:", sides_equal)
    print("Equal Angle Pairs:", angles_equal)
    print("Both Right Triangles:", right_triangle)

    sufficient = False
    method = ""

    if sides_equal == 3:
        sufficient = True
        method = "SSS"

    elif sides_equal >= 2 and angles_equal >= 1:
        sufficient = True
        method = "SAS"

    elif angles_equal >= 2 and sides_equal >= 1:
        sufficient = True
        method = "ASA or AAS"

    elif right_triangle == "yes" and sides_equal >= 2:
        sufficient = True
        method = "RHS"

    if sufficient:
        print("\nResult: Sufficient data is available.")
        print("Possible Congruence Rule:", method)
        print("The given evidence can establish triangle congruence.")
    else:
        print("\nResult: Insufficient data.")
        print("The given evidence does not establish triangle congruence.")
        print("Additional side or angle information is required.")

    print("\nData Sufficiency Check Completed.")

insufficientdatadetector()