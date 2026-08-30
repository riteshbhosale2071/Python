def pythagoreantriplechecker():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("All sides must be positive integers.")
        return

    sides = sorted([a, b, c])

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("The numbers form a Pythagorean Triple.")
    else:
        print("The numbers do not form a Pythagorean Triple.")

pythagoreantriplechecker()