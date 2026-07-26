def linesegment():
    length1 = float(input("Enter first line segment length: "))
    length2 = float(input("Enter second line segment length: "))

    if length1 > length2:
        print("First line segment is longer")
    elif length2 > length1:
        print("Second line segment is longer")
    else:
        print("Both line segments are equal")

linesegment()