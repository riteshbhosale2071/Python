def find():
    t = ("apple", "plane", "grape")

    common = set(t[0])

    for word in t[1:]:
        common = common & set(word)

    print("Common Characters:", tuple(common))

find()