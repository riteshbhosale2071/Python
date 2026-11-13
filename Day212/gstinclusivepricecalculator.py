def gstinclusivepricecalculator():
    try:
        total_price = float(input("Enter GST inclusive price (₹): "))
        gst_rate = float(input("Enter GST rate (%): "))

        if total_price < 0 or gst_rate < 0:
            print("Price and GST rate cannot be negative.")
            return

        if gst_rate == 0:
            original_price = total_price
            gst_amount = 0
        else:
            original_price = total_price / (1 + gst_rate / 100)
            gst_amount = total_price - original_price

        print("\nGST Inclusive Price Details")
        print("Total Price: ₹", round(total_price, 2))
        print("GST Rate:", gst_rate, "%")
        print("Original Price: ₹", round(original_price, 2))
        print("GST Amount: ₹", round(gst_amount, 2))
        print("CGST: ₹", round(gst_amount / 2, 2))
        print("SGST: ₹", round(gst_amount / 2, 2))

    except ValueError:
        print("Please enter valid numeric values.")

gstinclusivepricecalculator()