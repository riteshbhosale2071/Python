def rain():
    drops = int(input("Enter number of rain drops counted each minute: "))

    minutes = int(input("Enter number of minutes: "))

    total_drops = drops * minutes

    print("Total Rain Drops =", total_drops)

rain()