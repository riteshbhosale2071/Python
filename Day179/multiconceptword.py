def multiconceptword():
    print("Multi-Concept Word Problem :")

    print("1. Shopping Problem")
    print("2. Travel Problem")
    print("3. Investment Problem")
    print("4. Business Problem")

    choice = int(input("Select problem type: "))

    if choice == 1:
        price = float(input("Enter price of one item: "))
        quantity = int(input("Enter quantity: "))
        discount = float(input("Enter discount percentage: "))
        tax = float(input("Enter tax percentage: "))

        if price <= 0 or quantity <= 0 or discount < 0 or tax < 0:
            print("Enter valid values.")
            return

        subtotal = price * quantity
        discount_amount = subtotal * discount / 100
        after_discount = subtotal - discount_amount
        tax_amount = after_discount * tax / 100
        final_amount = after_discount + tax_amount

        print("\nWord Problem:")
        print("A customer buys", quantity, "items at", price, "each.")
        print("The store gives a", discount, "% discount and adds", tax, "% tax.")
        print("Find the final amount to be paid.")

        print("\nAnswer:", round(final_amount, 2))

    elif choice == 2:
        distance = float(input("Enter distance: "))
        speed = float(input("Enter speed: "))
        fuel_efficiency = float(input("Enter fuel efficiency (km/litre): "))
        fuel_price = float(input("Enter fuel price per litre: "))

        if distance <= 0 or speed <= 0 or fuel_efficiency <= 0 or fuel_price < 0:
            print("Enter valid values.")
            return

        time = distance / speed
        fuel_used = distance / fuel_efficiency
        fuel_cost = fuel_used * fuel_price

        print("\nWord Problem:")
        print("A vehicle travels", distance, "km at", speed, "km/h.")
        print("It gives a mileage of", fuel_efficiency, "km/litre.")
        print("Find the travel time and fuel cost.")

        print("\nTravel Time:", round(time, 2), "hours")
        print("Fuel Used:", round(fuel_used, 2), "litres")
        print("Fuel Cost:", round(fuel_cost, 2))

    elif choice == 3:
        principal = float(input("Enter investment amount: "))
        rate = float(input("Enter annual interest rate: "))
        years = float(input("Enter investment period: "))

        if principal <= 0 or rate < 0 or years <= 0:
            print("Enter valid values.")
            return

        interest = principal * rate * years / 100
        final_amount = principal + interest

        print("\nWord Problem:")
        print("A person invests", principal, "at", rate, "% simple interest")
        print("for", years, "years.")
        print("Find the interest earned and final amount.")

        print("\nInterest Earned:", round(interest, 2))
        print("Final Amount:", round(final_amount, 2))

    elif choice == 4:
        revenue = float(input("Enter total revenue: "))
        expenses = float(input("Enter total expenses: "))
        tax_rate = float(input("Enter tax percentage: "))

        if revenue < 0 or expenses < 0 or tax_rate < 0:
            print("Enter valid values.")
            return

        profit = revenue - expenses
        tax = 0

        if profit > 0:
            tax = profit * tax_rate / 100

        final_profit = profit - tax

        print("\nWord Problem:")
        print("A business earns", revenue, "in revenue and spends", expenses, ".")
        print("It pays", tax_rate, "% tax on its profit.")
        print("Find the final profit or loss.")

        print("\nProfit Before Tax:", round(profit, 2))
        print("Tax:", round(tax, 2))
        print("Final Profit/Loss:", round(final_profit, 2))

        if final_profit > 0:
            print("Result: Profit")
        elif final_profit < 0:
            print("Result: Loss")
        else:
            print("Result: Break-even")

    else:
        print("Invalid problem type.")

multiconceptword()