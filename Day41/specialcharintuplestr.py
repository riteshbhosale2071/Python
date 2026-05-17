def count():
    t = ("hello@", "python#", "code123", "data!")

    count = 0

    for word in t:
        for ch in word:

            if not ch.isalnum():
                count += 1

    print("Special Characters:", count)

count()