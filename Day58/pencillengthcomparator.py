def pencil():
    pencil1 = float(input("Enter length of Pencil 1 (cm): "))
    pencil2 = float(input("Enter length of Pencil 2 (cm): "))

    if pencil1 > pencil2:
        print("Pencil 1 is longer")

    elif pencil2 > pencil1:
        print("Pencil 2 is longer")

    else:
        print("Both pencils are of equal length")

pencil()