def find():
    t = (135, 246, 579, 111, 908)

    result = []

    for num in t:
        odd_only = True

        for digit in str(num):

            if int(digit) % 2 == 0:
                odd_only = False
                break

        if odd_only:
            result.append(num)

    print(tuple(result))

find()