def count():
    t = ("apple", "python", "education")

    count = 0

    for word in t:

        for ch in word.lower():

            if ch.isalpha() and ch not in "aeiou":
                count += 1

    print("Total Consonants:", count)

count()