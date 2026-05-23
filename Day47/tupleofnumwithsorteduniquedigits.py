def find():
    t = (1223, 4551, 9877)

    result = []

    for num in t:
        unique_digits = sorted(set(str(num)))
        result.append(int("".join(unique_digits)))

    print(tuple(result))

find()