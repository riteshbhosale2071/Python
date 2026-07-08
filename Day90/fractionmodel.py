def fractionmodel():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    print("Fraction:", numerator, "/", denominator)

    print("Model: ", end="")
    for i in range(denominator):
        if i < numerator:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

fractionmodel()