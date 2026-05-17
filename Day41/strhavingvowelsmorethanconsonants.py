def find():
    t = ("idea", "apple", "sky", "education")

    result = []

    for word in t:
        vowels = 0
        consonants = 0

        for ch in word.lower():

            if ch in "aeiou":
                vowels += 1
            elif ch.isalpha():
                consonants += 1

        if vowels > consonants:
            result.append(word)

    print(tuple(result))

find()