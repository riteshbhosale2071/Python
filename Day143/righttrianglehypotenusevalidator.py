import math

def righttrianglehypotenusevalidator():
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    hypotenuse = float(input("Enter the hypotenuse: "))

    if base <= 0 or height <= 0 or hypotenuse <= 0:
        print("All sides must be positive.")
        return

    calculated_hypotenuse = math.sqrt(base ** 2 + height ** 2)

    print("Calculated Hypotenuse:", calculated_hypotenuse)

    if math.isclose(calculated_hypotenuse, hypotenuse, rel_tol=1e-9):
        print("Valid Hypotenuse.")
        print("The given sides form a right triangle.")
    else:
        print("Invalid Hypotenuse.")
        print("The given sides do not form a right triangle.")

righttrianglehypotenusevalidator()