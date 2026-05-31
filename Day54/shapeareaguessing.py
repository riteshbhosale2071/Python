def game():
    shape = input("Enter shape (circle/square/rectangle): ").lower()

    if shape == "circle":

        r = float(input("Enter radius: "))
        area = 3.14 * r * r

    elif shape == "square":

        s = float(input("Enter side: "))
        area = s * s

    elif shape == "rectangle":

        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        area = l * b

    else:
        print("Invalid Shape")
        exit()

    print("Area =", area)

game()