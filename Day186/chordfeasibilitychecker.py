def chordfeasibilitychecker():
    print("Chord Feasibility Checker :")

    radius = float(input("Enter circle radius: "))
    chord_length = float(input("Enter proposed chord length: "))

    if radius <= 0:
        print("Invalid input: Radius must be greater than zero.")
        return

    if chord_length < 0:
        print("Invalid input: Chord length cannot be negative.")
        return

    diameter = 2 * radius

    print("\nFeasibility Analysis :")
    print("Circle Radius:", round(radius, 2))
    print("Circle Diameter:", round(diameter, 2))
    print("Proposed Chord Length:", round(chord_length, 2))

    if chord_length == 0:
        print("Result: Zero-length chord; it represents a single point.")
        print("Feasibility: Degenerate case.")
    elif chord_length > diameter:
        print("Result: Impossible chord length.")
        print("Feasibility: FAILED — chord cannot exceed the diameter.")
    else:
        distance = (radius ** 2 - (chord_length / 2) ** 2) ** 0.5
        print("Feasibility: PASSED")
        print("Perpendicular Distance from Center:", round(distance, 4))

        if abs(chord_length - diameter) < 0.000001:
            print("Chord Type: Diameter")
        else:
            print("Chord Type: Minor or major chord segment.")

        print("Half Chord Length:", round(chord_length / 2, 4))

    print("\nMaximum Possible Chord Length:", round(diameter, 2))

chordfeasibilitychecker()