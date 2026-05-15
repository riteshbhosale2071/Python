def find():
    t = (15, 42, 58, 91, 75, 100)

    result = []

    for num in t:
        if '5' in str(num):
            result.append(num)

    print("Numbers containing 5:", tuple(result))

find()