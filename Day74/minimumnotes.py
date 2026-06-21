def min():
    amount = int(input("Enter amount: "))

    notes500 = amount // 500
    amount %= 500

    notes200 = amount // 200
    amount %= 200

    notes100 = amount // 100
    amount %= 100

    notes50 = amount // 50
    amount %= 50

    notes20 = amount // 20
    amount %= 20

    notes10 = amount // 10
    amount %= 10

    print("500 Notes =", notes500)
    print("200 Notes =", notes200)
    print("100 Notes =", notes100)
    print("50 Notes =", notes50)
    print("20 Notes =", notes20)
    print("10 Notes =", notes10)

min()