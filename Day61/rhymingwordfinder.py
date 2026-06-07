def rhyming():
    word = input("Enter a word: ").lower()

    words = ["cat", "bat", "hat", "rat", "mat", "dog"]

    ending = word[-2:]

    print("Rhyming Words:")

    for w in words:
        if w.endswith(ending) and w != word:
            print(w)

rhyming()