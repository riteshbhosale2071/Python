def count():
    t = (4, 9, 10, 15, 16)

    count = 0

    for num in t:
        factors = 0

        for i in range(1, num + 1):

            if num % i == 0:
                factors += 1

        if factors % 2 == 0:
            count += 1

    print("Count:", count)

count()