def  day():
    time = int(input("Enter hour (0-23): "))

    if 6 <= time < 18:
        print("Day Time - Sun is Up")

    else:
        print("Night Time - Moon is Up")

day()