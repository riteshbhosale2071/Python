def replace():
    t = (2, 4, 5, 6, 7, 8, 9)

    result = []

    for num in t:
        prime = True

        if num < 2:
            prime = False

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            result.append(0)
        else:
            result.append(num)

    print(tuple(result))

replace()