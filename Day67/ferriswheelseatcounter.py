def wheel():
    seats_per_cabin = int(input("Enter seats per cabin: "))
    
    cabins = int(input("Enter number of cabins: "))

    total_seats = seats_per_cabin * cabins

    print("Total Seats =", total_seats)

wheel()