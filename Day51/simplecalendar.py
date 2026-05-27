def create():
    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]

    days = [31,28,31,30,31,30,31,31,30,31,30,31]

    month_no = int(input("Enter month number (1-12): "))

    print("Month =", months[month_no - 1])
    print("Days =", days[month_no - 1])

create()