def bus():
    rows = int(input("Enter number of rows: "))
    seats_per_row = int(input("Enter seats per row: "))

    seat_no = 1

    for i in range(rows):

        for j in range(seats_per_row):
            print(seat_no, end="\t")
            seat_no += 1

        print()

bus()