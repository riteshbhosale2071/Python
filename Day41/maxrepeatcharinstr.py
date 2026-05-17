def find():
    t = ("apple", "banana", "success")

    for word in t:
        max_char = max(set(word), key=word.count)

        print(word, "->", max_char)

find()