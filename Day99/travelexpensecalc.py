def travelexpense():
    transport = float(input("Enter transport expense: "))
    hotel = float(input("Enter hotel expense: "))
    food = float(input("Enter food expense: "))

    total = transport + hotel + food

    print("Total Travel Expense =", total)

travelexpense()