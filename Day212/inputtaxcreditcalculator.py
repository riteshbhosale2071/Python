def inputtaxcreditcalculator():
    try:
        purchase_amount = float(input("Enter purchase amount (₹): "))
        purchase_gst_rate = float(input("Enter purchase GST rate (%): "))
        sales_amount = float(input("Enter sales amount (₹): "))
        sales_gst_rate = float(input("Enter sales GST rate (%): "))

        if min(purchase_amount, purchase_gst_rate, sales_amount, sales_gst_rate) < 0:
            print("Values cannot be negative.")
            return

        input_tax = purchase_amount * purchase_gst_rate / 100
        output_tax = sales_amount * sales_gst_rate / 100

        input_tax_credit = input_tax
        net_gst_payable = max(0, output_tax - input_tax_credit)
        excess_credit = max(0, input_tax_credit - output_tax)

        print("\nInput Tax Credit Details")
        print("Purchase Amount: ₹", round(purchase_amount, 2))
        print("Input GST: ₹", round(input_tax, 2))
        print("Sales Amount: ₹", round(sales_amount, 2))
        print("Output GST: ₹", round(output_tax, 2))
        print("Available Input Tax Credit: ₹", round(input_tax_credit, 2))
        print("Net GST Payable: ₹", round(net_gst_payable, 2))
        print("Excess ITC: ₹", round(excess_credit, 2))

    except ValueError:
        print("Please enter valid numeric values.")

inputtaxcreditcalculator()