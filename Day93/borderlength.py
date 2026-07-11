def borderlength():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    border = 2 * (length + width)

    print("Border Length:", border)

borderlength()