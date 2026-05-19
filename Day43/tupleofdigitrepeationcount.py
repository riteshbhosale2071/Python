def count():
    t = (1223, 4555, 7899)

    result = []

    for num in t:
        repeated = 0

        for digit in str(num):

            if str(num).count(digit) > 1:
                repeated += 1

        result.append(repeated)

    print(tuple(result))

count()