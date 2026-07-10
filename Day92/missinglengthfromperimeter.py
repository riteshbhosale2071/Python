def missinglength():
    perimeter = float(input("Enter perimeter of rectangle: "))
    width = float(input("Enter width: "))

    length = (perimeter / 2) - width

    print("Missing Length:", length)

missinglength()