def find():
    t = (121, 345, 455, 789, 999)

    count = 0

    for num in t:

        if len(str(num)) != len(set(str(num))):
            count += 1

    print("Count:", count)

find()