def bakery():
    bread = int(input("Enter quantity of bread: "))
    cake = int(input("Enter quantity of cake: "))
    cookies = int(input("Enter quantity of cookies: "))

    bread_price = 30
    cake_price = 250
    cookies_price = 10

    total = (bread * bread_price) + (cake * cake_price) + (cookies * cookies_price)

    print("\nBakery Bill")
    print("Bread   =", bread * bread_price)
    print("Cake    =", cake * cake_price)
    print("Cookies =", cookies * cookies_price)
    print("Total Bill = ₹", total)

bakery()