def find():
    objects = {
        "Tree": 15,
        "Building": 50,
        "Pole": 10,
        "Tower": 80
    }

    tallest = max(objects, key=objects.get)
    shortest = min(objects, key=objects.get)

    print("Tallest Object =", tallest, "-", objects[tallest])
    print("Shortest Object =", shortest, "-", objects[shortest])

find()