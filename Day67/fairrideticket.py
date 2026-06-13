def fair():
    tickets = int(input("Enter number of ride tickets: "))
    
    price_per_ticket = float(input("Enter price per ticket: ₹"))

    total = tickets * price_per_ticket

    print("Total Ticket Cost = ₹", total)

fair()