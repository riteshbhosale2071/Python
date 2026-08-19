import math

def circleradius():
    circumference = float(input("Enter the circumference of the circle: "))

    if circumference <= 0:
        print("Circumference must be positive.")
        return

    radius = circumference / (2 * math.pi)

    print("Radius of the Circle:", radius)

circleradius()