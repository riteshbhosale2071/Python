def yearlyamount():
    print("Yearly Amount Tracker :")

    total = 0

    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    for month in months:
        amount = float(input("Enter amount for " + month + ": "))
        total += amount

    average = total / 12

    print("\nYearly Summary :")
    print("Total Amount:", round(total, 2))
    print("Average Monthly Amount:", round(average, 2))

    if total > 0:
        print("Yearly Status: Amount recorded successfully.")
    elif total == 0:
        print("Yearly Status: No amount recorded.")
    else:
        print("Yearly Status: Negative amount recorded.")

yearlyamount()