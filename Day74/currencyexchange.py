def exchange():
    amount = float(input("Enter amount in INR: ₹"))

    usd_rate = 83.0

    usd = amount / usd_rate

    print("Amount in USD = $", round(usd, 2))

exchange()