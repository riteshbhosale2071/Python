def compoundrectangle():
    length1 = float(input("Enter length of first rectangle: "))
    width1 = float(input("Enter width of first rectangle: "))
    length2 = float(input("Enter length of second rectangle: "))
    width2 = float(input("Enter width of second rectangle: "))

    total_area = (length1 * width1) + (length2 * width2)

    print("Total Area:", total_area)

compoundrectangle()