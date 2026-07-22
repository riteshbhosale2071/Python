def weeklytimetable():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    activity = input("Enter activity: ")

    print("Weekly Timetable")
    for day in days:
        print(day, "-", activity)

weeklytimetable()