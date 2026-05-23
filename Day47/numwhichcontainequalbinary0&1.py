def find():
    t = (5, 6, 9, 10, 12)

    result = []

    for num in t:
        binary = bin(num)[2:]

        if binary.count("0") == binary.count("1"):
            result.append(num)

    print(tuple(result))

find()