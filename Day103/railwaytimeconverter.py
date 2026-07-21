def railwaytime():
    hour = int(input("Enter railway time (0-23): "))

    if hour == 0:
        print("12 AM")
    elif hour < 12:
        print(hour, "AM")
    elif hour == 12:
        print("12 PM")
    else:
        print(hour - 12, "PM")

railwaytime()