def find():
    t = (23, 44, 56, 71, 89)

    result = []

    for num in t:
        total = sum(int(d) for d in str(num))

        prime = True

        if total < 2:
            prime = False

        for i in range(2, total):

            if total % i == 0:
                prime = False
                break

        if prime:
            result.append(num)

    print(tuple(result))

find()