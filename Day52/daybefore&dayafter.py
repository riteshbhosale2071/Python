def find():
    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    day = input("Enter day: ").capitalize()

    if day in days:

        index = days.index(day)

        before = days[(index - 1) % 7]
        after = days[(index + 1) % 7]

        print("Day Before =", before)
        print("Day After =", after)

    else:
        print("Invalid Day")

find()