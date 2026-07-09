def fractionstrip():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    print("Fraction Strip:")

    for i in range(denominator):
        if i < numerator:
            print("[■]", end="")
        else:
            print("[ ]", end="")
    print()

fractionstrip()