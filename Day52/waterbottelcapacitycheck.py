def check():
    capacity = int(input("Enter bottle capacity (ml): "))
    water = int(input("Enter current water amount (ml): "))

    if water == capacity:
        print("Bottle is Full")

    elif water < capacity:
        print("Bottle is Not Full")
        print("Remaining Capacity =", capacity - water, "ml")

    else:
        print("Water exceeded bottle capacity")

check()