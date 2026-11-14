def facevalueandmarketvaluecomparator():
    try:
        company_name = input("Enter company name: ")
        face_value = float(input("Enter face value per share (₹): "))
        market_value = float(input("Enter market value per share (₹): "))
        number_of_shares = int(input("Enter number of shares: "))

        if face_value <= 0 or market_value < 0 or number_of_shares <= 0:
            print("Please enter valid share details.")
            return

        difference = market_value - face_value
        total_face_value = face_value * number_of_shares
        total_market_value = market_value * number_of_shares

        percentage_difference = (difference / face_value) * 100

        print("\nFace Value and Market Value Comparison")
        print("Company Name:", company_name)
        print("Face Value Per Share: ₹", round(face_value, 2))
        print("Market Value Per Share: ₹", round(market_value, 2))
        print("Number of Shares:", number_of_shares)
        print("Difference Per Share: ₹", round(difference, 2))
        print("Total Face Value: ₹", round(total_face_value, 2))
        print("Total Market Value: ₹", round(total_market_value, 2))
        print("Percentage Difference:", round(percentage_difference, 2), "%")

        if difference > 0:
            print("Market Status: Trading at a premium.")
        elif difference < 0:
            print("Market Status: Trading at a discount.")
        else:
            print("Market Status: Trading at face value.")

    except ValueError:
        print("Please enter valid numeric values.")

facevalueandmarketvaluecomparator()