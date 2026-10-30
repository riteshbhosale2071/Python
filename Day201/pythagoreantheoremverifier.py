def pythagoreantheoremverifier():
    print("Pythagorean Theorem Verifier")

    a = float(input("Enter first perpendicular side: "))
    b = float(input("Enter second perpendicular side: "))
    c = float(input("Enter hypotenuse: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid side lengths. All sides must be positive.")

    elif abs((a ** 2 + b ** 2) - (c ** 2)) < 0.000001:
        print("The given sides satisfy the Pythagorean Theorem.")
        print("It forms a right-angled triangle.")

    else:
        print("The given sides do not satisfy the Pythagorean Theorem.")

pythagoreantheoremverifier()