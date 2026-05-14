def find():
    L = [12.5, True, [13,15,18.2],[5,6],"Ram"]

    total = 0
    count = 0

    for value in L:
        if type(value) == list:
            for num in value:
                total += num
                count += 1
    
    print("Avg:",total/count)

find()