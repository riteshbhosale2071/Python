def channel():
    channels = {
        1: "News",
        2: "Sports",
        3: "Movies",
        4: "Music",
        5: "Kids"
    }

    number = int(input("Enter channel number: "))

    if number in channels:
        print("Channel:", channels[number])

    else:
        print("Channel not found")

channel()