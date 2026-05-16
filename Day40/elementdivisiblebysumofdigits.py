def find():
    t = (12, 18, 21, 111, 25)

    result = []

    for num in t:
        digit_sum = sum(int(d) for d in str(num))

        if num % digit_sum == 0:
            result.append(num)

    print("Divisible by Sum of Digits:")
    print(tuple(result))

find()