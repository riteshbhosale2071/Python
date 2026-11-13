def gstcalculator():
    try:
        amount = float(input("Enter original amount (₹): "))
        gst_rate = float(input("Enter GST rate (%): "))

        if amount < 0 or gst_rate < 0:
            print("Amount and GST rate cannot be negative.")
            return

        gst_amount = amount * gst_rate / 100
        total_amount = amount + gst_amount

        print("\nGST Calculation")
        print("Original Amount: ₹", round(amount, 2))
        print("GST Rate:", gst_rate, "%")
        print("GST Amount: ₹", round(gst_amount, 2))
        print("Total Amount: ₹", round(total_amount, 2))

        print("\nGST Breakdown:")
        print("CGST: ₹", round(gst_amount / 2, 2))
        print("SGST: ₹", round(gst_amount / 2, 2))

    except ValueError:
        print("Please enter valid numeric values.")

gstcalculator()