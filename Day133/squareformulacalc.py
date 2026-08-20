def squareformulacalc():
    side = float(input("Enter the side of the square: "))

    if side <= 0:
        print("Side must be positive.")
        return

    area = side ** 2
    perimeter = 4 * side

    print("Area of Square:", area)
    print("Perimeter of Square:", perimeter)

squareformulacalc()