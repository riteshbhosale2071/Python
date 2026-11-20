import math

def quadraticrootcalculator():
    print("Quadratic Root Calculator")
    print("Standard Form: ax² + bx + c = 0")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Invalid quadratic equation: a cannot be zero.")
        return

    discriminant = b ** 2 - 4 * a * c

    print("\nDiscriminant =", discriminant)

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two distinct real roots:")
        print("Root 1 =", round(root1, 4))
        print("Root 2 =", round(root2, 4))

    elif discriminant == 0:
        root = -b / (2 * a)
        print("Two equal real roots:")
        print("Root 1 =", round(root, 4))
        print("Root 2 =", round(root, 4))

    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(-discriminant) / (2 * abs(a))
        print("Two complex roots:")
        print("Root 1 =", complex(round(real, 4), round(imaginary, 4)))
        print("Root 2 =", complex(round(real, 4), round(-imaginary, 4)))

quadraticrootcalculator()