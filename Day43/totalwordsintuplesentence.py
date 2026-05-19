def count():
    t = (
        "Python is easy",
        "Tuple programs are interesting",
        "Practice daily"
    )

    count = 0

    for sentence in t:
        count += len(sentence.split())

    print("Total Words:", count)

count()