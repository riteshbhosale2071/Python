def change():
    bill = float(input("Enter bill amount: "))
    paid = float(input("Enter amount paid: "))

    if paid >= bill:

        change = paid - bill

        print("Change to return =", change)

    else:
        print("Insufficient payment")

change()