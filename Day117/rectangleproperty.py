def rectangleproperty():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    perimeter = 2 * (length + width)
    area = length * width

    print("It is a Rectangle.")
    print("Length:", length)
    print("Width:", width)
    print("Perimeter:", perimeter)
    print("Area:", area)

rectangleproperty()