def heronsformula():
    print("Heron's Formula Calculator")

    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Side lengths must be positive.")

    elif a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2

        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        print("Semi-perimeter:", s)
        print("Area of Triangle:", round(area, 2))

    else:
        print("Invalid triangle. The given sides cannot form a triangle.")

heronsformula()