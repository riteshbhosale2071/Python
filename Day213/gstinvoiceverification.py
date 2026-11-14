def gstinvoiceverification():
    try:
        invoice_number = input("Enter invoice number: ")
        seller_gstin = input("Enter seller GSTIN: ").strip().upper()
        buyer_gstin = input("Enter buyer GSTIN: ").strip().upper()

        taxable_amount = float(input("Enter taxable amount (₹): "))
        gst_rate = float(input("Enter GST rate (%): "))
        cgst = float(input("Enter CGST amount (₹): "))
        sgst = float(input("Enter SGST amount (₹): "))
        igst = float(input("Enter IGST amount (₹): "))
        invoice_total = float(input("Enter final invoice amount (₹): "))

        errors = []

        if not invoice_number.strip():
            errors.append("Invoice number is missing.")

        if len(seller_gstin) != 15:
            errors.append("Seller GSTIN must contain 15 characters.")

        if len(buyer_gstin) != 15:
            errors.append("Buyer GSTIN must contain 15 characters.")

        if min(taxable_amount, gst_rate, cgst, sgst, igst, invoice_total) < 0:
            errors.append("Amounts and GST rate cannot be negative.")

        if gst_rate > 100:
            errors.append("GST rate cannot exceed 100%.")

        if not errors:
            expected_gst = taxable_amount * gst_rate / 100
            actual_gst = cgst + sgst + igst
            expected_total = taxable_amount + actual_gst

            if abs(actual_gst - expected_gst) > 0.02:
                errors.append("GST amount does not match the entered GST rate.")

            if abs(invoice_total - expected_total) > 0.02:
                errors.append("Invoice total does not match taxable amount and GST.")

            if cgst > 0 and igst > 0:
                errors.append("CGST/SGST and IGST should not be charged together.")

            if igst > 0 and (cgst > 0 or sgst > 0):
                errors.append("Invalid GST tax distribution.")

            if cgst > 0 and sgst > 0:
                if abs(cgst - sgst) > 0.02:
                    errors.append("CGST and SGST amounts should be equal.")

        print("\nGST Invoice Verification Report")
        print("Invoice Number:", invoice_number)
        print("Seller GSTIN:", seller_gstin)
        print("Buyer GSTIN:", buyer_gstin)
        print("Taxable Amount: ₹", round(taxable_amount, 2))
        print("GST Rate:", gst_rate, "%")
        print("Total GST: ₹", round(cgst + sgst + igst, 2))
        print("Invoice Amount: ₹", round(invoice_total, 2))

        if errors:
            print("\nVerification Status: FAILED")
            for error in errors:
                print("-", error)
        else:
            print("\nVerification Status: PASSED")
            print("All basic invoice calculations are consistent.")

        print("\nNote: This program performs basic calculation checks.")
        print("It does not verify GSTIN authenticity or legal GST compliance.")

    except ValueError:
        print("Please enter valid numeric values.")

gstinvoiceverification()