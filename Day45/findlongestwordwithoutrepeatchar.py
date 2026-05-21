def find():
    t = ("apple", "lamp", "strength", "kite")

    longest = ""

    for word in t:

        if len(word) == len(set(word)):

            if len(word) > len(longest):
                longest = word

    print("Longest Word:", longest)

find()