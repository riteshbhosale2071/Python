def find():
    t = ("cat", "dog", "python", "abc")

    result = []

    for word in t:
        total = 0

        for ch in word:
            total += ord(ch)

        prime = True

        if total < 2:
            prime = False

        for i in range(2, total):

            if total % i == 0:
                prime = False
                break

        if prime:
            result.append(word)

    print(tuple(result))

find()