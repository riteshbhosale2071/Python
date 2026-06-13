def movie():
    tickets = int(input("Enter number of tickets: "))
    
    price = float(input("Enter ticket price: ₹"))

    total_cost = tickets * price

    print("Total Cost = ₹", total_cost)

movie()