def count():
    t = (123, 456, 222, 91)

    count = 0

    for num in t:
        digit_sum = 0
        product = 1

        for digit in str(num):
            digit_sum += int(digit)
            product *= int(digit)

        if product > digit_sum:
            count += 1

    print("Count:", count)

count()