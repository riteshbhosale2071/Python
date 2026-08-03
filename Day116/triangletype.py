def triangletype():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("The given sides do not form a triangle.")
    elif a == b == c:
        print("Triangle Type: Equilateral")
    elif a == b or b == c or a == c:
        print("Triangle Type: Isosceles")
    else:
        print("Triangle Type: Scalene")

triangletype()