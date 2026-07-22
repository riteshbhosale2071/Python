def watercapacity():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    capacity = length * width * height
    print("Water Capacity =", capacity, "liters")

watercapacity()