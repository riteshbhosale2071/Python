def birthday():
    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]

    month_no = int(input("Enter birth month number (1-12): "))

    print("Birthday Month =", months[month_no - 1])

birthday()