def wind():
    speed = float(input("Enter wind speed (km/h): "))

    if speed < 20:
        print("Category: Light Wind")

    elif speed < 40:
        print("Category: Moderate Wind")

    elif speed < 60:
        print("Category: Strong Wind")

    else:
        print("Category: Storm Wind")

wind()