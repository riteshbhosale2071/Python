def find():
    t = (1234, 2468, 1357, 9087)

    result = []

    for num in t:
        even = 0
        odd = 0

        for digit in str(num):

            if int(digit) % 2 == 0:
                even += 1
            else:
                odd += 1

        if even > odd:
            result.append(num)

    print(tuple(result))

find()