def calculateduration(start_hour, start_minute, end_hour, end_minute):
    start_time = start_hour * 60 + start_minute
    end_time = end_hour * 60 + end_minute

    duration = end_time - start_time

    hours = duration // 60
    minutes = duration % 60

    print("Duration =", hours, "hours", minutes, "minutes")

h1 = int(input("Enter start hour: "))
m1 = int(input("Enter start minute: "))
h2 = int(input("Enter end hour: "))
m2 = int(input("Enter end minute: "))

calculateduration(h1, m1, h2, m2)