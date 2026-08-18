def bestdealfinder():
    items = input("Enter item names separated by spaces: ").split()
    prices = list(map(float, input("Enter prices separated by spaces: ").split()))

    if len(items) != len(prices):
        print("Number of items and prices must be equal.")
        return

    if not items or any(price < 0 for price in prices):
        print("Please enter valid item names and prices.")
        return

    minimum_price = min(prices)
    index = prices.index(minimum_price)

    print("Best Deal:", items[index])
    print("Lowest Price:", minimum_price)

bestdealfinder()