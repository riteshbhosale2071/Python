def calculatelength(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return (dx ** 2 + dy ** 2) ** 0.5

def checkcongruence(length1, length2, tolerance=0.000001):
    return abs(length1 - length2) <= tolerance

def main():
    print("Segment Congruence Checker")
    print("Enter the coordinates of the endpoints of two line segments.")

    print("\nFirst segment:")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    print("\nSecond segment:")
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))
    x4 = float(input("Enter x4: "))
    y4 = float(input("Enter y4: "))

    length1 = calculatelength(x1, y1, x2, y2)
    length2 = calculatelength(x3, y3, x4, y4)

    print("\nLength of first segment:", round(length1, 4))
    print("Length of second segment:", round(length2, 4))

    if checkcongruence(length1, length2):
        print("The two line segments are congruent.")
    else:
        print("The two line segments are not congruent.")

main()