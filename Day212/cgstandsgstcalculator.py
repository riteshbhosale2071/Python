def cgstandsgstcalculator():
    try:
        amount = float(input("Enter original amount (₹): "))
        gst_rate = float(input("Enter total GST rate (%): "))

        if amount < 0 or gst_rate < 0:
            print("Amount and GST rate cannot be negative.")
            return

        cgst_rate = gst_rate / 2
        sgst_rate = gst_rate / 2

        cgst_amount = amount * cgst_rate / 100
        sgst_amount = amount * sgst_rate / 100

        total_gst = cgst_amount + sgst_amount
        total_amount = amount + total_gst

        print("\nCGST and SGST Details")
        print("Original Amount: ₹", round(amount, 2))
        print("Total GST Rate:", gst_rate, "%")
        print("CGST Rate:", cgst_rate, "%")
        print("SGST Rate:", sgst_rate, "%")
        print("CGST Amount: ₹", round(cgst_amount, 2))
        print("SGST Amount: ₹", round(sgst_amount, 2))
        print("Total GST: ₹", round(total_gst, 2))
        print("Final Amount: ₹", round(total_amount, 2))

    except ValueError:
        print("Please enter valid numeric values.")

cgstandsgstcalculator()