def divide():
    t = (12, 18, 24, 111)

    result = []

    for num in t:
        digit_sum = 0

        for digit in str(num):
            digit_sum += int(digit)

        result.append(round(num / digit_sum, 2))

    print(tuple(result))

divide()