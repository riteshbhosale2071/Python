def donationrecord():
    donors = int(input("Enter number of donors: "))
    amount = float(input("Enter donation amount per donor: "))

    total_donation = donors * amount

    print("Number of Donors:", donors)
    print("Total Donation:", total_donation)

donationrecord()