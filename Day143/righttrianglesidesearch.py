import math

def righttrianglesidesearch():
    hypotenuse = float(input("Enter the hypotenuse: "))

    if hypotenuse <= 0:
        print("Hypotenuse must be positive.")
        return

    found = False

    print("Possible integer side pairs:")

    for base in range(1, int(hypotenuse)):
        height_squared = hypotenuse ** 2 - base ** 2
        height = math.sqrt(height_squared)

        if math.isclose(height, round(height), rel_tol=1e-9):
            height = int(round(height))

            if height > 0:
                print(f"Base = {base}, Height = {height}")
                found = True

    if not found:
        print("No integer side pair found.")

righttrianglesidesearch()