def find():
    t = (135, 222, 579, 246)

    result = []

    for num in t:
        product = 1

        for digit in str(num):
            product *= int(digit)

        if product % 2 != 0:
            result.append(num)

    print(tuple(result))

find()