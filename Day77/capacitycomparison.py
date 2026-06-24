def comparison():
    capacity1 = float(input("Enter capacity of Container 1 (liters): "))
    capacity2 = float(input("Enter capacity of Container 2 (liters): "))

    if capacity1 > capacity2:
        print("Container 1 has greater capacity")

    elif capacity2 > capacity1:
        print("Container 2 has greater capacity")

    else:
        print("Both containers have the same capacity")

comparison()