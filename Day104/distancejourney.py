def distanceplanner():
    speed = float(input("Enter speed (km/h): "))
    time = float(input("Enter time (hours): "))

    distance = speed * time
    print("Distance Travelled =", distance, "km")

distanceplanner()