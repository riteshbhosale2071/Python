def parallelogramproperty():
    base = float(input("Enter the base of the parallelogram: "))
    side = float(input("Enter the side length: "))
    height = float(input("Enter the height: "))

    perimeter = 2 * (base + side)
    area = base * height

    print("It is a Parallelogram.")
    print("Base:", base)
    print("Side:", side)
    print("Height:", height)
    print("Perimeter:", perimeter)
    print("Area:", area)

parallelogramproperty()