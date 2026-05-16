def count():
    t = ("apple", "python", "education")

    count = 0

    for word in t:
        for ch in word:
            if ch.lower() in "aeiou":
                count += 1

    print("Total Vowels:", count)

count()