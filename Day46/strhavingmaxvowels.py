def find():

    t = ("education", "apple", "beautiful", "python")

    max_vowels = 0
    answer = ""

    for word in t:
        count = 0

        for ch in word.lower():

            if ch in "aeiou":
                count += 1

        if count > max_vowels:
            max_vowels = count
            answer = word

    print("Word:", answer)
    print("Vowels:", max_vowels)

find()