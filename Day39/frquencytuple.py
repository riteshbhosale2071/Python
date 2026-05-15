def find():
    t = ("a", "b", "a", "c", "b", "a")

    freq = []

    for ch in set(t):
        freq.append((ch, t.count(ch)))

    print(tuple(freq))

find()