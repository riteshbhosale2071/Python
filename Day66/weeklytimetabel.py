def timetable():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for day in days:
        subject = input(f"Enter subject for {day}: ")
        print(day, ":", subject)

timetable()