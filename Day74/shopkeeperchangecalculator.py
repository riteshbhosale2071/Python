def change():
    bill_amount = float(input("Enter bill amount: ₹"))
    
    paid_amount = float(input("Enter paid amount: ₹"))

    change = paid_amount - bill_amount

    print("Change to Return = ₹", change)

change()