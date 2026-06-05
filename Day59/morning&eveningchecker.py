def check():
    hour = int(input("Enter hour (0-23): "))

    if 5 <= hour < 12:
        print("Morning")

    elif 12 <= hour < 18:
        print("Evening")

    else:
        print("Night")

check()