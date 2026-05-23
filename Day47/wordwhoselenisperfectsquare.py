def count():
    t = ("hi", "code", "apple", "banana", "education")

    count = 0

    for word in t:
        length = len(word)

        if int(length ** 0.5) ** 2 == length:
            count += 1

    print("Count:", count)

count()