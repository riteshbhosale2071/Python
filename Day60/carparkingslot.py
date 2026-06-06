def parking():
    slots = int(input("Enter total parking slots: "))
    
    parked = int(input("Enter parked cars: "))

    free = slots - parked

    print("Occupied Slots =", parked)

    print("Free Slots =", free)

parking()