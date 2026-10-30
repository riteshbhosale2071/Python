def trianglevalidity():
    print("Triangle Validity Checker")

    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid triangle. Side lengths must be positive.")

    elif a + b > c and a + c > b and b + c > a:
        print("The given sides form a valid triangle.")

        if a == b == c:
            print("Triangle Type: Equilateral")
        elif a == b or b == c or a == c:
            print("Triangle Type: Isosceles")
        else:
            print("Triangle Type: Scalene")

    else:
        print("The given sides do not form a valid triangle.")

trianglevalidity()