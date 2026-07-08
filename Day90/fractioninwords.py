def readfraction():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    print("Fraction:", numerator, "/", denominator)

    if denominator == 2:
        print("In Words:", numerator, "half")
    elif denominator == 3:
        print("In Words:", numerator, "third")
    elif denominator == 4:
        print("In Words:", numerator, "fourth")
    elif denominator == 5:
        print("In Words:", numerator, "fifth")
    elif denominator == 6:
        print("In Words:", numerator, "sixth")
    elif denominator == 7:
        print("In Words:", numerator, "seventh")
    elif denominator == 8:
        print("In Words:", numerator, "eighth")
    elif denominator == 9:
        print("In Words:", numerator, "ninth")
    elif denominator == 10:
        print("In Words:", numerator, "tenth")
    else:
        print("Denominator not supported.")

readfraction()