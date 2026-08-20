def pythagoreantriangle():
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("All sides must be positive.")
        return

    sides = sorted([a, b, c])

    if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9:
        print("The triangle is a Pythagorean (Right-Angled) Triangle.")
    else:
        print("The triangle is not a Pythagorean Triangle.")

pythagoreantriangle()