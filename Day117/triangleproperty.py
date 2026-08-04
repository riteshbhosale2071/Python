def triangleproperty():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("The given sides do not form a valid triangle.")
        return

    perimeter = a + b + c

    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    print("Triangle is Valid")
    print("Triangle Type:", triangle_type)
    print("Perimeter:", round(perimeter, 2))

triangleproperty()