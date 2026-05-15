def find():
    t = (2, 5, 8, 10)

    binary = []

    for num in t:
        binary.append(bin(num)[2:])

    print(tuple(binary))

find()