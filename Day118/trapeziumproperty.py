def trapeziumproperty():
    side1 = float(input("Enter the first parallel side: "))
    side2 = float(input("Enter the second parallel side: "))
    side3 = float(input("Enter the third side: "))
    side4 = float(input("Enter the fourth side: "))
    height = float(input("Enter the height: "))

    perimeter = side1 + side2 + side3 + side4
    area = ((side1 + side2) * height) / 2

    print("It is a Trapezium.")
    print("Perimeter:", perimeter)
    print("Area:", area)

trapeziumproperty()