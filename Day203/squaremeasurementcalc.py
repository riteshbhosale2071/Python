import math

def squaremeasurementcalc():
    side = float(input("Enter the side length of the square: "))

    if side <= 0:
        print("Invalid measurement. Side length must be positive.")
        return

    area = side ** 2
    perimeter = 4 * side
    diagonal = side * math.sqrt(2)

    print("\nSquare Measurement Report")
    print(f"Side Length: {side:.2f}")
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")
    print(f"Diagonal: {diagonal:.2f}")
    print("All four sides are equal.")
    print("Each interior angle is 90 degrees.")

squaremeasurementcalc()