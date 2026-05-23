def count():
    t = (2, 4, 5, 6, 10)

    count = 0

    for num in t:

        if str(num ** 3)[-1] == str(num)[-1]:
            count += 1

    print("Count:", count)

count()