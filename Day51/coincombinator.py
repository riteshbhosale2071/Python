def find():
    amount = int(input("Enter amount: "))

    coins = [10, 5, 2, 1]

    for coin in coins:

        count = amount // coin

        amount = amount % coin

        print(coin, "rupee coin =", count)

find()