def find():
    t = ("sky", "apple", "gym", "rhythm", "orange")

    result = []

    for word in t:
        has_vowel = False

        for ch in word.lower():

            if ch in "aeiou":
                has_vowel = True
                break

        if not has_vowel:
            result.append(word)

    print(tuple(result))

find()