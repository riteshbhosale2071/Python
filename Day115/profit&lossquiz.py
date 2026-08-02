def profitlossquiz():
    cost_price = 500
    selling_price = 650

    print("Quiz Question:")
    print("Cost Price =", cost_price)
    print("Selling Price =", selling_price)
    answer = input("Is it Profit or Loss? ").lower()

    if selling_price > cost_price:
        correct = "profit"
    elif selling_price < cost_price:
        correct = "loss"
    else:
        correct = "no profit no loss"

    if answer == correct:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer:", correct.title())

profitlossquiz()