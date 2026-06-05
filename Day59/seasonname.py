def name():
    month = input("Enter month name: ").capitalize()

    if month in ["December", "January", "February"]:
        print("Season = Winter")

    elif month in ["March", "April", "May"]:
        print("Season = Summer")

    elif month in ["June", "July", "August", "September"]:
        print("Season = Monsoon")

    elif month in ["October", "November"]:
        print("Season = Autumn")

    else:
        print("Invalid Month")

name()