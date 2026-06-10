def battery():
    battery = int(input("Enter battery percentage: "))

    if battery >= 80:
        print("Battery Level: High")

    elif battery >= 30:
        print("Battery Level: Medium")

    else:
        print("Battery Level: Low")

battery()