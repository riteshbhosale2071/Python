def igstcalculator():
    try:
        amount = float(input("Enter original amount (₹): "))
        igst_rate = float(input("Enter IGST rate (%): "))

        if amount < 0 or igst_rate < 0:
            print("Amount and IGST rate cannot be negative.")
            return

        igst_amount = amount * igst_rate / 100
        total_amount = amount + igst_amount

        print("\nIGST Calculation")
        print("Original Amount: ₹", round(amount, 2))
        print("IGST Rate:", igst_rate, "%")
        print("IGST Amount: ₹", round(igst_amount, 2))
        print("Total Amount: ₹", round(total_amount, 2))

    except ValueError:
        print("Please enter valid numeric values.")

igstcalculator()