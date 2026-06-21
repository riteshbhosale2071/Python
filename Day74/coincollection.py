def coin():
    coins = []

    n = int(input("Enter number of coins: "))

    for i in range(n):
        coin = int(input(f"Enter value of coin {i+1}: "))
        coins.append(coin)

    print("Total Coins =", len(coins))
    print("Total Value = ₹", sum(coins))
    print("Highest Value Coin = ₹", max(coins))
    print("Lowest Value Coin = ₹", min(coins))

coin()