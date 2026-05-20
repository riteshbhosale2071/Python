def find():
    t = ("apple", "boat", "sky", "paper", "moon")

    result = []

    for word in t:
        vowels = 0

        for ch in word.lower():

            if ch in "aeiou":
                vowels += 1

        if vowels == 2:
            result.append(word)

    print(tuple(result))

find()