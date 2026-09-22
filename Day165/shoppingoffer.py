def shoppingoffer():
    print("Shopping Offer Simulator :")

    marked_price = float(input("Enter the marked price: "))
    quantity = int(input("Enter the quantity: "))

    if marked_price > 0 and quantity > 0:
        total_price = marked_price * quantity

        print("\nChoose an offer:")
        print("1. Flat Percentage Discount")
        print("2. Buy 2 Get 1 Free")
        print("3. Buy 3 Get 1 Free")
        print("4. Flat Discount Amount")

        choice = input("Enter your choice: ")

        if choice == "1":
            discount_percentage = float(input("Enter discount percentage: "))

            if 0 <= discount_percentage <= 100:
                discount_amount = total_price * discount_percentage / 100
                final_price = total_price - discount_amount

                print("Original Price:", round(total_price, 2))
                print("Discount Amount:", round(discount_amount, 2))
                print("Final Price:", round(final_price, 2))
            else:
                print("Invalid discount percentage.")

        elif choice == "2":
            free_items = quantity // 3
            payable_items = quantity - free_items
            final_price = payable_items * marked_price

            print("Free Items:", free_items)
            print("Payable Items:", payable_items)
            print("Original Price:", round(total_price, 2))
            print("Final Price:", round(final_price, 2))
            print("Total Savings:", round(total_price - final_price, 2))

        elif choice == "3":
            free_items = quantity // 4
            payable_items = quantity - free_items
            final_price = payable_items * marked_price

            print("Free Items:", free_items)
            print("Payable Items:", payable_items)
            print("Original Price:", round(total_price, 2))
            print("Final Price:", round(final_price, 2))
            print("Total Savings:", round(total_price - final_price, 2))

        elif choice == "4":
            flat_discount = float(input("Enter flat discount amount: "))

            if 0 <= flat_discount <= total_price:
                final_price = total_price - flat_discount

                print("Original Price:", round(total_price, 2))
                print("Discount Amount:", round(flat_discount, 2))
                print("Final Price:", round(final_price, 2))
            else:
                print("Invalid discount amount.")

        else:
            print("Invalid offer choice.")
    else:
        print("Price and quantity must be greater than zero.")

shoppingoffer()