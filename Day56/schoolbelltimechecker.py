def find():
    bell_times = [
        "09:00",
        "10:00",
        "11:00",
        "12:00",
        "01:00"
    ]

    time = input("Enter current time (HH:MM): ")

    if time in bell_times:
        print("School Bell Rings!")

    else:
        print("No Bell at this time")

find()