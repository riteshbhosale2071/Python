def sales():
    n = int(input("Enter number of sales: "))

    sales = []

    for i in range(n):
        amount = float(input(f"Enter sale amount {i+1}: "))
        sales.append(amount)

    print("\nSales Report")
    print("-" * 30)

    print("Sales Data:", sales)
    print("Highest Sale =", max(sales))
    print("Lowest Sale =", min(sales))
    print("Total Sales =", sum(sales))
    print("Average Sale =", round(sum(sales) / n, 2))

sales()