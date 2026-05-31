def checker():
    day = input("Enter day: ").capitalize()

    weekend = ["Saturday", "Sunday"]

    if day in weekend:
        print("Weekend")

    else:
        print("Weekday")

checker()