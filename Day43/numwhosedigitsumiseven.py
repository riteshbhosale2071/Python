def find():
    t = (123, 456, 789, 246)

    result = []

    for num in t:
        digit_sum = 0

        for digit in str(num):
            digit_sum += int(digit)

        if digit_sum % 2 == 0:
            result.append(num)

    print(tuple(result))

find()