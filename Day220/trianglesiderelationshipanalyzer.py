def trianglesiderelationshipanalyzer():
    print("Triangle Side Relationship Analyzer")

    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    if min(a, b, c) <= 0:
        print("All side lengths must be positive.")
        return

    sides = sorted([a, b, c])
    x, y, z = sides

    print("\nTriangle Side Analysis:")
    print("Smallest Side =", x)
    print("Middle Side =", y)
    print("Largest Side =", z)

    if x + y <= z:
        print("Invalid Triangle: Triangle inequality is not satisfied.")
        return

    print("\nTriangle Inequality:")
    print(f"{x} + {y} > {z}")
    print("Valid triangle.")

    if x == y == z:
        print("Type: Equilateral Triangle")
    elif x == y or y == z or x == z:
        print("Type: Isosceles Triangle")
    else:
        print("Type: Scalene Triangle")

    if x ** 2 + y ** 2 == z ** 2:
        print("Angle Classification: Right-Angled Triangle")
    elif x ** 2 + y ** 2 > z ** 2:
        print("Angle Classification: Acute-Angled Triangle")
    else:
        print("Angle Classification: Obtuse-Angled Triangle")

    print("\nSide Relationship:")
    print("Sum of two smaller sides =", x + y)
    print("Difference between largest and smallest sides =", z - x)

trianglesiderelationshipanalyzer()