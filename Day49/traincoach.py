def find():
    train = [
        "Engine",
        "S1",
        "S2",
        "S3",
        "A1",
        "B1",
        "GEN"
    ]

    coach = input("Enter coach name: ")

    if coach in train:
        print("Coach Position =", train.index(coach) + 1)

    else:
        print("Coach not found")

find()