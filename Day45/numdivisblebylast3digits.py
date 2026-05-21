def count():
    t = (12, 25, 36, 41, 84)

    count = 0

    for num in t:
        last = int(str(num)[-1])

        if last != 0 and num % last == 0:
            count += 1

    print("Count:", count)

count()