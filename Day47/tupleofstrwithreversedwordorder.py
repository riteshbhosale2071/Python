def tuplefun():
    t = (
        "Python is easy",
        "Tuple programs are fun",
        "Practice every day"
    )

    result = []

    for sentence in t:
        words = sentence.split()
        reverse = " ".join(words[::-1])

        result.append(reverse)

    print(tuple(result))

tuplefun()