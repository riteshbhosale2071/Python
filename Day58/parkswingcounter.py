def swing():
    swings = int(input("Enter total swings in the park: "))

    occupied = int(input("Enter occupied swings: "))

    free = swings - occupied

    print("Occupied Swings =", occupied)
    
    print("Free Swings =", free)

swing()