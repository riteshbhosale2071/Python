def find():
    t = (12, 35, 46, 57, 80, 91)

    count = 0

    for num in t:

        if int(str(num)[-1]) % 2 == 0:
            count += 1

    print("Count:", count)

find()