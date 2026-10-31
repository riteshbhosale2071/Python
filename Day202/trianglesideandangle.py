import math

def trianglesideandangle():
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = float(input("Enter side C: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid triangle. Side lengths must be positive.")
        return

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle. The triangle inequality is not satisfied.")
        return

    angle_a = math.degrees(
        math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    )
    angle_b = math.degrees(
        math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    )
    angle_c = 180 - angle_a - angle_b

    perimeter = a + b + c
    semi_perimeter = perimeter / 2
    area = math.sqrt(
        semi_perimeter
        * (semi_perimeter - a)
        * (semi_perimeter - b)
        * (semi_perimeter - c)
    )

    print("\nTriangle Side and Angle Report")
    print(f"Side A: {a:.2f} | Angle A: {angle_a:.2f} degrees")
    print(f"Side B: {b:.2f} | Angle B: {angle_b:.2f} degrees")
    print(f"Side C: {c:.2f} | Angle C: {angle_c:.2f} degrees")
    print(f"Perimeter: {perimeter:.2f}")
    print(f"Area: {area:.2f}")

    if a == b == c:
        print("Triangle Type: Equilateral")
    elif a == b or b == c or a == c:
        print("Triangle Type: Isosceles")
    else:
        print("Triangle Type: Scalene")

trianglesideandangle()