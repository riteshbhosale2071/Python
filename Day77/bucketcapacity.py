def bucket():
    capacity = float(input("Enter bucket capacity (liters): "))
    
    water = float(input("Enter current water amount (liters): "))

    percentage = (water / capacity) * 100

    print("Bucket Filled =", round(percentage, 2), "%")

bucket()