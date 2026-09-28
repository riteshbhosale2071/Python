def congruenceevidenceanalyzer():
    print("Congruence Evidence Analyzer :")

    print("\nEnter the available evidence for two triangles.")

    side1 = float(input("Enter first side of Triangle 1: "))
    side2 = float(input("Enter corresponding first side of Triangle 2: "))

    side3 = float(input("Enter second side of Triangle 1: "))
    side4 = float(input("Enter corresponding second side of Triangle 2: "))

    side5 = float(input("Enter third side of Triangle 1: "))
    side6 = float(input("Enter corresponding third side of Triangle 2: "))

    angle1 = float(input("Enter first angle of Triangle 1: "))
    angle2 = float(input("Enter corresponding first angle of Triangle 2: "))

    angle3 = float(input("Enter second angle of Triangle 1: "))
    angle4 = float(input("Enter corresponding second angle of Triangle 2: "))

    right1 = input("Is Triangle 1 a right triangle? (yes/no): ").lower()
    right2 = input("Is Triangle 2 a right triangle? (yes/no): ").lower()

    equal_side1 = side1 == side2
    equal_side2 = side3 == side4
    equal_side3 = side5 == side6

    equal_angle1 = angle1 == angle2
    equal_angle2 = angle3 == angle4

    print("\nEvidence Analysis :")

    print("First pair of sides equal:", equal_side1)
    print("Second pair of sides equal:", equal_side2)
    print("Third pair of sides equal:", equal_side3)
    print("First pair of angles equal:", equal_angle1)
    print("Second pair of angles equal:", equal_angle2)

    if equal_side1 and equal_side2 and equal_side3:
        print("\nCongruence Evidence: SSS")
        print("Conclusion: The triangles are congruent by SSS.")

    elif equal_side1 and equal_side2 and equal_angle1:
        print("\nCongruence Evidence: SAS")
        print("Conclusion: The triangles may be congruent by SAS.")

    elif equal_angle1 and equal_angle2 and equal_side1:
        print("\nCongruence Evidence: ASA")
        print("Conclusion: The triangles may be congruent by ASA.")

    elif right1 == "yes" and right2 == "yes" and equal_side1 and equal_side2:
        print("\nCongruence Evidence: RHS")
        print("Conclusion: The triangles may be congruent by RHS.")

    elif equal_angle1 and equal_angle2:
        print("\nEvidence: Two corresponding angles are equal.")
        print("Conclusion: Congruence is not established from this evidence alone.")

    elif equal_side1 and equal_side2:
        print("\nEvidence: Two corresponding sides are equal.")
        print("Conclusion: Congruence is not established from this evidence alone.")

    else:
        print("\nConclusion: The provided evidence is insufficient to establish congruence.")

    print("\nEvidence Analysis Completed.")

congruenceevidenceanalyzer()