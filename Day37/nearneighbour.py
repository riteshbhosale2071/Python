import math

def find():
    neighbors = [(1, 2), (4, 6), (5, 1), (7, 3)]

    point = (3, 4)

    nearest = None
    min_distance = float('inf')

    for n in neighbors:

        distance = math.sqrt(
            (n[0] - point[0])**2 +
            (n[1] - point[1])**2
        )

        if distance < min_distance:
            min_distance = distance
            nearest = n

    print("Nearest Neighbor =", nearest)
    print("Distance =", min_distance)

find()