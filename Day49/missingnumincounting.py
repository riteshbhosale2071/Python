def find():
    L = [1, 2, 3, 5, 6]

    n = max(L)

    for i in range(1, n + 1):

        if i not in L:
            print("Missing Number =", i)

find()