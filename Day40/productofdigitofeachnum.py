def find():
    t = (123, 45, 67)

    for num in t:
        product = 1

        for digit in str(num):
            product *= int(digit)

        print("Product of digits of", num, "=", product)

find()