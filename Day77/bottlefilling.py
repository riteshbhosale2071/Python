def bottle():
    total_water = float(input("Enter total water (liters): "))
    
    bottle_capacity = float(input("Enter bottle capacity (liters): "))

    bottles = total_water // bottle_capacity

    print("Total Bottles Filled =", int(bottles))

bottle()