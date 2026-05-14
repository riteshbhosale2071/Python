def convert():
    t = ((1, 2, 3),
     (4, 5, 6),
     (7, 8, 9))

    spiral = []

    for i in t[0]:
        spiral.append(i)

    for i in range(1, len(t)):
        spiral.append(t[i][-1])

    for i in reversed(t[-1][:-1]):
        spiral.append(i)

    print("Spiral Order:", tuple(spiral))

convert()