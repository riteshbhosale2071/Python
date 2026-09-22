def multiproductdiscountcalc():
    print("Multi-Product Discount Calculator :")

    number_of_products = int(input("Enter the number of products: "))

    if number_of_products > 0:
        total_original_price = 0
        total_discount = 0
        total_final_price = 0

        for i in range(1, number_of_products + 1):
            print("\nProduct", i)

            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))
            discount_percentage = float(input("Enter discount percentage: "))

            if price > 0 and quantity > 0 and 0 <= discount_percentage <= 100:
                original_price = price * quantity
                discount_amount = original_price * discount_percentage / 100
                final_price = original_price - discount_amount

                total_original_price += original_price
                total_discount += discount_amount
                total_final_price += final_price

                print("Original Price:", round(original_price, 2))
                print("Discount Amount:", round(discount_amount, 2))
                print("Final Price:", round(final_price, 2))
            else:
                print("Invalid product details.")

        print("\n=== Purchase Summary ===")
        print("Total Original Price:", round(total_original_price, 2))
        print("Total Discount:", round(total_discount, 2))
        print("Total Final Price:", round(total_final_price, 2))

        if total_original_price > 0:
            effective_discount = (total_discount / total_original_price) * 100
            print("Effective Discount Percentage:", round(effective_discount, 2), "%")
    else:
        print("Number of products must be greater than zero.")

multiproductdiscountcalc()