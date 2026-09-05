import math

def parallellinedistanceconsistency():
    print("Parallel-Line Distance Consistency Checker :")

    n = int(input("Enter number of distance measurements: "))

    if n < 2:
        print("Enter at least 2 distance measurements.")
        return

    distances = []

    for i in range(n):
        distance = float(input(f"Enter distance {i + 1}: "))

        if distance <= 0:
            print("Distance must be positive.")
            return

        distances.append(distance)

    tolerance = float(input("Enter allowed tolerance: "))

    if tolerance < 0:
        print("Tolerance cannot be negative.")
        return

    reference = distances[0]

    print("\nDistance Consistency Analysis :")
    print("Reference Distance:", reference)

    consistent = True

    for i, distance in enumerate(distances, start=1):
        difference = abs(distance - reference)

        print(
            f"Distance {i}: {distance} | "
            f"Difference: {difference}"
        )

        if difference > tolerance:
            consistent = False

    print("\nResult :")

    if consistent:
        print("All distances are consistent.")
        print("The measurements support equal spacing between the parallel lines.")
    else:
        print("The distances are not consistent.")
        print("The measurements do not support equal spacing between the parallel lines.")

parallellinedistanceconsistency()