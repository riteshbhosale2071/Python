def count():
    t = ("apple", "banana", "success")

    count = 0

    for word in t:

        for ch in set(word):

            if word.count(ch) > 1:
                count += 1

    print("Total Repeating Characters:", count)

count()