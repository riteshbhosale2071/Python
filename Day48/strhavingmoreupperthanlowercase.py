def find():
    t = ("PyTHon", "CODE", "Data", "AI")

    result = []

    for word in t:
        upper = 0
        lower = 0

        for ch in word:

            if ch.isupper():
                upper += 1

            elif ch.islower():
                lower += 1

        if upper > lower:
            result.append(word)

    print(tuple(result))

find()