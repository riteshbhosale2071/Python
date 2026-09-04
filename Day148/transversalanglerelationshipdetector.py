def transversalanglerelationshipdetector():
    print("Transversal Angle Relationship Detector :")
    print("Enter two angles formed by a transversal.")

    angle1 = float(input("Enter first angle: "))
    angle2 = float(input("Enter second angle: "))

    if not (0 < angle1 < 180 and 0 < angle2 < 180):
        print("Angles must be between 0 and 180 degrees.")
        return

    print("\nAngle Relationship :")

    if angle1 == angle2:
        print("The angles may be Corresponding, Alternate Interior,")
        print("or Alternate Exterior angles.")
        print("Relationship: Equal Angles")

    elif angle1 + angle2 == 180:
        print("The angles may be Co-interior or Co-exterior angles.")
        print("Relationship: Supplementary Angles")

    else:
        print("No standard transversal angle relationship detected.")

transversalanglerelationshipdetector()