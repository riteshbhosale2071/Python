def ticket():
    ticket_price = int(input("Enter ticket price per person: "))
        
    passengers = int(input("Enter number of passengers: "))

    total = ticket_price * passengers

    print("Total Ticket Price = ₹", total)

ticket()