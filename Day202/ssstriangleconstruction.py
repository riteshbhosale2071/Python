def ssstriangleconstruction():
    print("SSS Triangle Construction Data")

    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Side lengths must be positive.")

    elif a + b > c and a + c > b and b + c > a:
        print("Triangle construction is possible.")

        perimeter = a + b + c
        s = perimeter / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        print("Perimeter:", round(perimeter, 2))
        print("Semi-perimeter:", round(s, 2))
        print("Area:", round(area, 2))

        if a == b == c:
            print("Triangle Type: Equilateral")
        elif a == b or b == c or a == c:
            print("Triangle Type: Isosceles")
        else:
            print("Triangle Type: Scalene")

    else:
        print("Triangle construction is not possible.")

ssstriangleconstruction()