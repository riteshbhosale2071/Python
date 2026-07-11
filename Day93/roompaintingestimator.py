def roompainting():
    length = float(input("Enter room length: "))
    width = float(input("Enter room width: "))
    cost = float(input("Enter painting cost per square unit: "))

    area = length * width
    totalcost = area * cost

    print("Room Area:", area)
    print("Painting Cost:", totalcost)

roompainting()