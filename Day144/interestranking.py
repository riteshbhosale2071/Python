def interestranking():
    n = int(input("Enter the number of investments: "))

    if n <= 0:
        print("Number of investments must be positive.")
        return

    investments = []

    for i in range(1, n + 1):
        print(f"\nInvestment {i}:")
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter interest rate (%): "))
        time = float(input("Enter time (years): "))

        if principal <= 0 or rate < 0 or time < 0:
            print("Invalid investment details.")
            return

        interest = (principal * rate * time) / 100
        investments.append((interest, i))

    # Sort investments by interest in descending order
    investments.sort(reverse=True)

    print("\n--- Interest Ranking ---")

    for rank, (interest, investment_no) in enumerate(investments, start=1):
        print(
            f"Rank {rank}: Investment {investment_no} "
            f"- Interest = {interest}"
        )

interestranking()