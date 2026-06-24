def container():
    capacity = float(input("Enter container capacity (liters): "))
    
    used = float(input("Enter water stored (liters): "))

    efficiency = (used / capacity) * 100

    print("Container Efficiency =", round(efficiency, 2), "%")

container()