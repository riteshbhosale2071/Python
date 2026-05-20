def find():
    t = (123, 45, 9, 88, 100)

    result = []

    for num in t:
        total = 0

        for digit in str(num):
            total += int(digit)

        if total > 10:
            result.append(num)

    print(tuple(result))

find()