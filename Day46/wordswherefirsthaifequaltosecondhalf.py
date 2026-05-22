def find():
    t = ("mama", "hello", "abab", "xyzxyz")

    result = []

    for word in t:

        if len(word) % 2 == 0:
            mid = len(word) // 2

            if word[:mid] == word[mid:]:
                result.append(word)

    print(tuple(result))

find()