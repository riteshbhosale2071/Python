def multistepshopping():
    print("Multi-Step Shopping Analyzer :")

    number_of_items = int(input("Enter number of items: "))

    if number_of_items <= 0:
        print("Enter a valid number of items.")
        return

    total = 0

    for i in range(number_of_items):
        print("\nItem", i + 1)

        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity <= 0:
            print("Enter valid price and quantity.")
            return

        item_total = price * quantity
        total += item_total

        print("Item Total:", round(item_total, 2))

    print("\nDiscount :")

    discount_rate = float(input("Enter discount percentage: "))

    if discount_rate < 0 or discount_rate > 100:
        print("Discount must be between 0 and 100.")
        return

    discount = total * discount_rate / 100
    discounted_total = total - discount

    print("\nTax :")

    tax_rate = float(input("Enter tax percentage: "))

    if tax_rate < 0:
        print("Tax cannot be negative.")
        return

    tax = discounted_total * tax_rate / 100
    final_amount = discounted_total + tax

    print("\nShopping Summary :")
    print("Subtotal:", round(total, 2))
    print("Discount:", round(discount, 2))
    print("Amount After Discount:", round(discounted_total, 2))
    print("Tax:", round(tax, 2))
    print("Final Amount:", round(final_amount, 2))

    if final_amount >= 10000:
        print("Purchase Category: High Value")
    elif final_amount >= 5000:
        print("Purchase Category: Medium Value")
    else:
        print("Purchase Category: Regular Purchase")

multistepshopping()