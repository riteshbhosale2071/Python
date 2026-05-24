def find():
    t = ("education", "apple", "idea", "orange")

    result = []

    for word in t:
        vowels = []

        for ch in word.lower():

            if ch in "aeiou":
                vowels.append(ch)

        if len(vowels) == len(set(vowels)):
            result.append(word)

    print(tuple(result))

find()