def find():
    t = ("apple", "banana", "lamp", "strength")

    result = []

    for word in t:
        unique = len(set(word))

        prime = True

        if unique < 2:
            prime = False

        for i in range(2, unique):

            if unique % i == 0:
                prime = False
                break

        if prime:
            result.append(word)

    print(tuple(result))

find()