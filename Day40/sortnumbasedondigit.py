def find():
    t = (1234, 5, 67, 89012, 456)

    sorted_tuple = tuple(sorted(t, key=lambda x: len(str(x))))

    print(sorted_tuple)

find()