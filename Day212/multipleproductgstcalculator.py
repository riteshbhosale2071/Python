def multipleproductgstcalculator():
    try:
        total_taxable_amount = 0
        total_gst_amount = 0

        products = int(input("Enter number of products: "))

        if products <= 0:
            print("Number of products must be greater than zero.")
            return

        print("\nMultiple Product GST Calculation")

        for i in range(1, products + 1):
            print(f"\nProduct {i}")

            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit (₹): "))
            gst_rate = float(input("Enter GST rate (%): "))

            if quantity <= 0 or price < 0 or gst_rate < 0:
                print("Invalid product details.")
                return

            taxable_amount = quantity * price
            gst_amount = taxable_amount * gst_rate / 100
            total_amount = taxable_amount + gst_amount

            total_taxable_amount += taxable_amount
            total_gst_amount += gst_amount

            print("Product Name:", name)
            print("Taxable Amount: ₹", round(taxable_amount, 2))
            print("GST Amount: ₹", round(gst_amount, 2))
            print("Product Total: ₹", round(total_amount, 2))

        grand_total = total_taxable_amount + total_gst_amount

        print("\nGST SUMMARY :")
        print("Total Products:", products)
        print("Total Taxable Amount: ₹", round(total_taxable_amount, 2))
        print("Total GST Amount: ₹", round(total_gst_amount, 2))
        print("Grand Total Amount: ₹", round(grand_total, 2))
        print("CGST: ₹", round(total_gst_amount / 2, 2))
        print("SGST: ₹", round(total_gst_amount / 2, 2))

    except ValueError:
        print("Please enter valid numeric values.")

multipleproductgstcalculator()