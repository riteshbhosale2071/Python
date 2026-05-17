def find():
    t = ("apple", "table", "grape", "code", "dance")

    result = []

    for i in range(len(t)):
        for j in range(i + 1, len(t)):

            if t[i][-1] == t[j][-1]:
                result.append((t[i], t[j]))

    print("Pairs with Same Ending Letter:")
    print(tuple(result))

find()