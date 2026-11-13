def gsttaxinvoice():
    try:
        seller_name = input("Enter seller name: ").strip()
        buyer_name = input("Enter buyer name: ").strip()
        invoice_number = input("Enter invoice number: ").strip()
        product_name = input("Enter product name: ").strip()

        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter price per unit (₹): "))
        gst_rate = float(input("Enter GST rate (%): "))

        if not seller_name or not buyer_name or not invoice_number or not product_name:
            print("All invoice details are required.")
            return

        if quantity <= 0 or price < 0 or gst_rate < 0:
            print("Enter valid quantity, price, and GST rate.")
            return

        taxable_amount = quantity * price
        gst_amount = taxable_amount * gst_rate / 100
        cgst = gst_amount / 2
        sgst = gst_amount / 2
        total_amount = taxable_amount + gst_amount

        print("\n" + "=" * 45)
        print("                 GST TAX INVOICE")
        print("=" * 45)
        print("Invoice Number :", invoice_number)
        print("Seller Name    :", seller_name)
        print("Buyer Name     :", buyer_name)
        print("-" * 45)
        print("Product Name   :", product_name)
        print("Quantity       :", quantity)
        print("Unit Price     : ₹", round(price, 2))
        print("Taxable Amount : ₹", round(taxable_amount, 2))
        print("-" * 45)
        print("GST Rate       :", gst_rate, "%")
        print("CGST           : ₹", round(cgst, 2))
        print("SGST           : ₹", round(sgst, 2))
        print("-" * 45)
        print("Total GST      : ₹", round(gst_amount, 2))
        print("Grand Total    : ₹", round(total_amount, 2))
        print("Thank you for your purchase!")

    except ValueError:
        print("Please enter valid numeric values.")

gsttaxinvoice()