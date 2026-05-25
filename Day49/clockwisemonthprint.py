def create():
    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]

    start = int(input("Enter starting month number (1-12): "))

    for i in range(12):

        print(months[(start - 1 + i) % 12])

create()