def find():
    t = (5, 10, 7, 11)

    result = []

    for num in t:
        binary = bin(num)[2:]

        valid = True

        for i in range(len(binary) - 1):

            if binary[i] == binary[i + 1]:
                valid = False
                break

        if valid:
            result.append(num)

    print(tuple(result))

find()