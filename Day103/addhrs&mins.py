def addtime():
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))

    total_minutes = hours * 60 + minutes

    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60

    print("Time =", new_hours, "hours", new_minutes, "minutes")

addtime()