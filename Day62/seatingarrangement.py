def seating():
    students = int(input("Enter number of students: "))
    seats_per_row = int(input("Enter seats per row: "))

    seat = 1

    for i in range(students):

        print(seat, end="\t")
        seat += 1

        if i % seats_per_row == seats_per_row - 1:
            print()

seating()