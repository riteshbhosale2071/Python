def find():
    items = [1, 2, 1, 3, 2, 4, 3]

    pairs = 0
    used = []

    for i in items:

        if i not in used and items.count(i) >= 2:

            pairs += 1
            used.append(i)

    print("Total Pairs =", pairs)

find()