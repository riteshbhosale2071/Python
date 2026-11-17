def gstbillingandinvoicemanagement():
    print("GST Billing and Invoice Management System")

    seller_name = input("Enter seller name: ")
    seller_gstin = input("Enter seller GSTIN: ")
    buyer_name = input("Enter buyer name: ")
    buyer_gstin = input("Enter buyer GSTIN: ")
    invoice_number = input("Enter invoice number: ")

    n = int(input("Enter number of products: "))

    if n <= 0:
        print("Please enter a positive number of products.")
        return

    products = []
    subtotal = 0
    total_gst = 0

    for i in range(n):
        print(f"\nProduct {i + 1}")
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        gst_rate = float(input("Enter GST rate (%): "))

        if quantity <= 0 or price < 0 or gst_rate < 0 or gst_rate > 100:
            print("Invalid product details.")
            return

        amount = quantity * price
        gst = amount * gst_rate / 100
        total = amount + gst

        products.append((name, quantity, price, gst_rate, amount, gst, total))

        subtotal += amount
        total_gst += gst

    grand_total = subtotal + total_gst

    print("\nGST Tax Invoice:")
    print("Invoice Number:", invoice_number)
    print("Seller Name:", seller_name)
    print("Seller GSTIN:", seller_gstin)
    print("Buyer Name:", buyer_name)
    print("Buyer GSTIN:", buyer_gstin)

    print("\nProduct Details:")
    print(f"{'Product':<15}{'Qty':<8}{'Price':<10}{'GST %':<10}{'Amount':<12}{'GST':<12}{'Total':<12}")

    for product in products:
        name, quantity, price, rate, amount, gst, total = product
        print(f"{name:<15}{quantity:<8}{price:<10.2f}{rate:<10.2f}{amount:<12.2f}{gst:<12.2f}{total:<12.2f}")

    print("\nInvoice Summary:")
    print("Subtotal:", round(subtotal, 2))
    print("Total GST:", round(total_gst, 2))
    print("Grand Total:", round(grand_total, 2))
    print("Invoice generated successfully.")

gstbillingandinvoicemanagement()