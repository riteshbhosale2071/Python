def rhombusproperty():
    side = float(input("Enter the side length of the rhombus: "))
    diagonal1 = float(input("Enter the first diagonal: "))
    diagonal2 = float(input("Enter the second diagonal: "))

    perimeter = 4 * side
    area = (diagonal1 * diagonal2) / 2

    print("It is a Rhombus.")
    print("Side Length:", side)
    print("Perimeter:", perimeter)
    print("Area:", area)

rhombusproperty()